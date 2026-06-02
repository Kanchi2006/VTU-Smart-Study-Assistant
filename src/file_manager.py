import os

NOTES_FOLDER = "uploads/notes"
PYQ_FOLDER = "uploads/pyqs"


def create_folders():

    os.makedirs(NOTES_FOLDER, exist_ok=True)
    os.makedirs(PYQ_FOLDER, exist_ok=True)


def save_uploaded_file(uploaded_file, upload_type):

    create_folders()

    if upload_type == "Notes":
        folder = NOTES_FOLDER
    else:
        folder = PYQ_FOLDER

    file_path = os.path.join(folder, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path