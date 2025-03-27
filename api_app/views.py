from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Student, Subject
from .serializers import StudentSerializer, SubjectSerializer

@api_view(['GET'])
def studentsfn(request):
    if Student.objects.count() == 0:
        students_data = [
            {"name": "Daud Deusdedith", "program": "COMPUTER NETWORKS AND SECURITY ENGINEERING"},
            {"name": "Raphaeli Philipo", "program": "CYBER SECURITY ENGINEERING"},
            {"name": "abubakari Hassan", "program": "INFORMATION SYSTEM"},
            {"name": "Maria Shayo", "program": "HEALTH INFORMATION SYSTEM"},
            {"name": "James Sanga", "program": "BUSSINESS INFORMATION SYSTEM"},
            {"name": "Nasibu Omary", "program": "SOFTWARE ENGINEERING"},
            {"name": "Michael Johnson", "program": "TELECOMMUNICATION ENGINEERING"},
            {"name": "Sophia Daud", "program": "COMPUTER SCIENCE"},
            {"name": "Aisha Gumbo", "program": "MULTIMEDIA TECHNOLOGY"},
            {"name": "Mathew Chami", "program": "COMPUTER ENGINEERING"},
        ]
        for student in students_data:
            Student.objects.create(name=student["name"], program=student["program"])

    students = Student.objects.all()[:10]

    serializer = StudentSerializer(students, many=True)

    return render(request, 'students.html', {'students': serializer.data})

@api_view(['GET'])
def subjectsfn(request):
    # Check if subjects exist, if not, insert them
    if Subject.objects.count() == 0:
        subjects_data = [
            {"subject_name": "Introduction to Programming", "year": 1},
            {"subject_name": "Computer Networks", "year": 1},
            {"subject_name": "Mathematics for Computing", "year": 1},
            {"subject_name": "Digital Logic Design", "year": 1},
            {"subject_name": "Communication Skills", "year": 1},

            {"subject_name": "Software Engineering Fundamentals", "year": 2},
            {"subject_name": "Data Structures & Algorithms", "year": 2},
            {"subject_name": "Database Management Systems", "year": 2},
            {"subject_name": "Operating Systems", "year": 2},
            {"subject_name": "Object-Oriented Programming", "year": 2},
            {"subject_name": "Web Development", "year": 2},

            {"subject_name": "Software Project Management", "year": 3},
            {"subject_name": "Advanced Software Engineering", "year": 3},
            {"subject_name": "Cybersecurity Basics", "year": 3},
            {"subject_name": "Mobile Application Development", "year": 3},

            {"subject_name": "Cloud Computing", "year": 4},
            {"subject_name": "Machine Learning", "year": 4},
            {"subject_name": "Cybersecurity for Developers", "year": 4},
            {"subject_name": "Artificial Intelligence", "year": 4},
            {"subject_name": "Big Data Analytics", "year": 4},
            {"subject_name": "Internet of Things", "year": 4},
            {"subject_name": "Human-Computer Interaction", "year": 4},
            {"subject_name": "Blockchain Technology", "year": 4},
            {"subject_name": "Software Testing & Quality Assurance", "year": 4},
            {"subject_name": "Ethical Hacking", "year": 4},
            {{"subject_name": "Database Security", "year": 4}}
        ]
        for subject in subjects_data:
            Subject.objects.create(subject_name=subject["subject_name"], year=subject["year"])

    # Retrieve all subjects ordered by year
    subjects = Subject.objects.all().order_by('year')

    # Structure the subjects for the template
    structured_data = {}
    for subject in subjects:
        year = f"Year {subject.year}"
        if year not in structured_data:
            structured_data[year] = []
        structured_data[year].append(subject.subject_name)

    # Render the subjects.html file with the subjects data
    return render(request, 'subjects.html', {'subjects': structured_data})

