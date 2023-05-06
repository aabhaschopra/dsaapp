from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from datetime import datetime
from components.get_event_details import get_event_details
from components.conf import db
from heads.views import isHead
from dsa.views import isDSA


def isStudent(request):
    if not isDSA(request) and not isHead(request):
        return True
    
    return False


def student_final_view_data(request, sid):
    eventsOrganized = []
    eventsParticipated = []

    collection_name = db["students"]
    students = collection_name.find({})

    collection_name = db["events"]

    for student in students:    
        if student["sid"] == sid:
            eventsOrganized = []
            eventsParticipated = []
            if len(student["events_organization"]) > 0:
                for event in student["events_organization"]:
                    eventsOrganized.append(get_event_details(event))
                
                eventsOrganized = sorted(eventsOrganized, key=lambda x: datetime.strptime(x["date"], '%d-%m-%Y'))

            if len(student["events_participation"]) > 0:
                for event in student["events_participation"]:
                    eventsParticipated.append(get_event_details(event))

                eventsParticipated = sorted(eventsParticipated, key=lambda x: datetime.strptime(x["date"], '%d-%m-%Y'))
            
            endpoint = request.get_full_path().rsplit("/", 1)[0]
            print("endpoint: {}".format(endpoint))
            if endpoint == "/student/{}/organized_events".format(sid):
                html = "student_organized_events.html"

            elif endpoint == "/student/{}/participated_events".format(sid):
                html = "student_participated_events.html"
            
            else:
                html = "student_landing_page.html"
            
            return render(request, html, {"student": student, "eventsOrganized": eventsOrganized, "eventsParticipated": eventsParticipated, "isStudent": isStudent(request)})


def student_view_data(request):
    collection_name = db["students"]
    students = collection_name.find({})

    for student in students:
        if student["email"] == request.user.email:
            sid = student["sid"]
            return redirect(f"{sid}/")

    messages.error(request, "{} is not authenticated. Please contact DSA office.".format(request.user.email))
    logout(request)
    return HttpResponseRedirect("/")
