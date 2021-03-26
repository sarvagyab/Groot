# Groot
<img width="64" src="https://raw.githubusercontent.com/Lincoln2000/Groot--Markdown_Note_Management_System/master/Application/Icons/App Icon/groot_256.png" align="left" />Groot is a free, open source, markdown note management system developed with PySide2. It can handle a large no of documents, organized in notebooks and sub-notebooks. The notes are searchable with regex. Groot has been inspired from another great open source note management system made with Electron, [Joplin](https://github.com/laurent22/joplin).

Credit for Icons Set - <a target="_blank" href="https://all-free-download.com/free-icon/download/mono-icon-set-icons-pack_120933.html">Free Mono Icon Set</a> by <a target="_blank" href="https://gentleface.com">gentleface</a>

<div class="top-screenshot"><img src="https://raw.githubusercontent.com/Lincoln2000/Groot--Markdown_Note_Management_System/master/Application/Icons/App%20Icon/GrootApp.png" style="max-width: 100%; max-height: 35em;"></div>

## Installation

There are three ways to install Groot -

- Portable Version

    To give the app a quick trial, Portable version of the app can be downloaded from the [Release](https://github.com/Lincoln2000/Groot--Markdown_Note_Management_System/releases) section. It will create a folder "Application" in the same folder in which it is run.
    
- Full Installation
    
    For full installation of the app, Full version can be installed from the [Release](https://github.com/Lincoln2000/Groot--Markdown_Note_Management_System/releases) section.
   
- From Source Code

    - After downloading the source files, run 
    ` pip install -r requirements.txt` 
    from terminal in the topmost directory.  
    This will install the necessary dependencies for the app to run.
    - After all the dependencies are installed, to start the application, run
    `python cli.py` 
    from terminal in the topmost directory.
  
 ## Features
 
 ### Markdown
 
 The text written in the Editor(left) is rendered in realtime in the Markdown Viewer(right). The experience can be enhanced with the use of plugins available in settings. Note Links are also available for cross linking in notes. For more info, have a look at [Markdown Guide](https://github.com/Lincoln2000/Groot--Markdown_Note_Management_System/blob/master/Markdown%20Guide.md)
 
 ### Importing and Exporting
 
 Notes with markdown extension(.md) can be imported in the app in any notebook and subnotebook.  
 Notes can be exported in markdown(.md), HTML and PDF formats.
 
 ### Security
 
 Security has been the top priority in designing Groot. The app asks you for a password on its first run. By default, this password is used to encrypt all your notes on your storage. This is done so that the decrypted notes never exist on your storage. Only when you open a note, it is decrypted in RAM edited there and encrypted before putting back on the storage. This ensures total security from anyone accessing the notes outside the app even if someone gets access to your storage device. You can opt out of this encryption of all notes, but it is not recommended to do so.  
 The app requires a password for starting irrespective of encrypting notes or not for security purposes.  
For additional security, notes can be encrypted within the app too. If a note is encrypted inside the app, the note would require a password for decrypting before you can read it and make changes to it. Even if the user forgets to encrypt the note again, unless the user has removed the password, the app will encrypt all the decrypted automatically upon closing. This provides an extra layer of security to your notes.  
At all stages, standard AES encryption is used for top of the line security and protection.
 
 ### Subnotebooks
 
 Sub-notebooks allow a greater level of organizing. Each notebook and sub-notebook can have as many sub-notebooks as the user would like to have creating a hierarchy as per the users needs.
 
 ### Searching
 
 The notes are searchable with standard searching method as well as using regex.
 
 ### Attachments
  
 Attach files button can be used to attach any file to the note. Image files will be displayed in the note itself. The files once attached in a note will be deleted from the system when the note will be deleted.
