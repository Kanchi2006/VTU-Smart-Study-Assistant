VTU Smart Study Assistant
Project Overview

VTU Smart Study Assistant is an AI-powered Retrieval-Augmented Generation (RAG) platform designed specifically for VTU students.

The system allows students to upload semester notes, lab manuals, question banks, and study materials in PDF format and interact with them through a conversational interface.

Instead of manually searching through hundreds of pages of notes, students can ask questions in natural language and receive accurate answers derived directly from their uploaded documents.

The platform also generates VTU-style 5-mark and 10-mark answers, revision notes, and quiz questions, helping students prepare efficiently for examinations.

Problem Statement

VTU students face several challenges:

Information Overload

Students often have:

Notes
PPTs
PDFs
Question Banks
Lab Manuals

spread across multiple folders and subjects.

Finding a specific concept before exams is time-consuming.

Exam-Oriented Preparation

Students need:

2-mark answers
5-mark answers
10-mark answers

but preparing them manually requires reading entire units.

Lack of Personalized Learning Tools

Generic AI chatbots:

do not understand the VTU syllabus
may provide incorrect answers
are not based on the student's own notes

Students need a system that learns from their own study material.

Proposed Solution

VTU Smart Study Assistant uses RAG architecture to create a personalized academic assistant.

The user uploads VTU study materials.

The system:

Extracts text from PDFs
Splits content into chunks
Creates vector embeddings
Stores embeddings in FAISS
Retrieves relevant content during queries
Uses an LLM to generate context-aware answers

This ensures responses are grounded in the uploaded study materials.

Target Users
Primary Users
VTU Students
Engineering Students
Diploma Students
Secondary Users
Faculty Members
Teaching Assistants
Study Groups
Core Features
1. PDF Upload System

Students can upload:

Notes
Question Papers
Lab Manuals
Study Guides
Reference Books

Supported format:

PDF
2. AI Chat with Notes

Students can ask:

What is a Binary Search Tree?
Explain Dijkstra's Algorithm.
What are the applications of Graph Theory?

The assistant answers using uploaded notes.

3. VTU 5-Mark Answer Generator

Students enter:

Explain BFS.

System generates:

Exam-oriented 5-mark answer

with:

Introduction
Explanation
Advantages
Conclusion
4. VTU 10-Mark Answer Generator

Students enter:

Explain OSI Model.

System generates:

Detailed explanation
Diagrams (optional)
Advantages
Disadvantages
Applications

Suitable for semester exams.

5. Quiz Generator

Generate:

MCQs

Example:

10 MCQs from Unit 3
Short Questions

Example:

5 important viva questions
6. Revision Notes Generator

Converts large chapters into:

One-page revision notes

Useful before examinations.

7. Source Citation

Every answer includes:

Source:
Operating Systems Notes
Page 14

Improves trustworthiness.

Technical Architecture
                User
                  │
                  ▼
          Streamlit Frontend
                  │
                  ▼
           PDF Upload Module
                  │
                  ▼
          Text Extraction Layer
                  │
                  ▼
            Chunking Module
                  │
                  ▼
         Sentence Embeddings
                  │
                  ▼
             FAISS Index
                  │
                  ▼
          Retrieval Engine
                  │
                  ▼
             Gemini LLM
                  │
                  ▼
            Generated Answer
Technology Stack
Frontend
Python
Streamlit

Purpose:

Simple UI
Fast development
Backend
Python

Purpose:

Processing
Retrieval
LLM Integration
Document Processing
PyPDF

Purpose:

Extract text from PDFs
Embeddings
Sentence Transformers

Model Example:

all-MiniLM-L6-v2

Purpose:

Convert text into vectors.

Vector Database
FAISS

Purpose:

Store and retrieve embeddings efficiently.

Large Language Model

Possible Options:

Google Gemini
OpenAI GPT
Open-source LLMs

Recommended for hackathon:

Gemini Free Tier

Folder Structure
VTU-Smart-Study-Assistant/
│
├── app.py
│
├── uploads/
│
├── data/
│   ├── vectors/
│   └── processed/
│
├── src/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── answer_generator.py
│   ├── quiz_generator.py
│   └── notes_generator.py
│
├── assets/
│
├── requirements.txt
│
└── README.md
Expected Workflow
Step 1

Upload Notes

Graph Theory.pdf
Step 2

System Creates Vector Database

Embeddings Generated
Step 3

Student Asks

What is Vertex Cover?
Step 4

System Retrieves Relevant Chunks

Page 32
Page 33
Step 5

Gemini Generates Final Answer

Accurate answer based on uploaded notes
Future Scope

After the hackathon, the project can be expanded with:

Multi-subject support
Voice-based queries
Kannada language support
Mobile application
VTU syllabus mapping
Previous year question paper analysis
Personalized study plans
Semester-wise dashboards
