import os

apps_dict = {
    "notepad.exe": ["notepad", "text editor"],
    "winword.exe": ["wordpad", "rich text editor"],
    "mspaint.exe": ["paint", "mspaint"],
    "calc.exe": ["calculator", "calc"],
    "cmd.exe": ["command prompt", "cmd", "terminal"],
    "powershell.exe": ["powershell", "ps"],
    "taskmgr.exe": ["task manager", "manager"],
    "control.exe": ["control panel", "settings"],
    "start ms-settings:": ["settings", "windows settings"],
    "explorer.exe": ["file explorer", "windows explorer"],
    "snippingtool.exe": ["snipping tool", "screenshot tool"],
    "wmplayer.exe": ["windows media player", "media player"],
    "regedit.exe": ["registry editor", "regedit"],
    "msinfo32.exe": ["system information", "system info"],
    "devmgmt.msc": ["device manager", "hardware manager"],
    "diskmgmt.msc": ["disk management", "partition manager"],
    "windowsdefender://": ["windows security", "defender"],
    "eventvwr.msc": ["event viewer", "system logs"],
    "ms-windows-store:": ["microsoft store", "windows store"],
    "msedge.exe": ["edge", "microsoft edge", "browser"],
    "chrome.exe": ["chrome", "google chrome", "browser"],
    "firefox.exe": ["firefox", "mozilla firefox", "browser"],
    "opera.exe": ["opera", "opera browser"],
    "brave.exe": ["brave", "brave browser"],
    "winword.exe": ["word", "microsoft word", "document editor"],
    "excel.exe": ["excel", "microsoft excel", "spreadsheet"],
    "powerpnt.exe": ["powerpoint", "microsoft powerpoint", "presentation"],
    "outlook.exe": ["outlook", "microsoft outlook", "email client"],
    "onenote.exe": ["onenote", "microsoft onenote"],
    "code.exe": ["vscode", "visual studio code", "code editor"],
    "pycharm.exe": ["pycharm", "python ide"],
    "eclipse.exe": ["eclipse", "java ide"],
    "studio64.exe": ["android studio", "mobile development ide"],
    "idea64.exe": ["intellij idea", "java ide"],
    "git-bash.exe": ["git bash", "git terminal"],
    "xampp-control.exe": ["xampp", "xampp control panel"],
    "vlc.exe": ["vlc", "vlc media player"],
    "spotify.exe": ["spotify", "music player", "songs"],
    "netflix:": ["netflix", "netflix app"],
    "primevideo:": ["amazon prime", "prime video"],
    "7zFM.exe": ["7-zip", "7zip", "file manager"],
    "winrar.exe": ["winrar", "file extractor"],
    "AnyDesk.exe": ["anydesk", "remote desktop"],
    "TeamViewer.exe": ["teamviewer", "remote access"],
    "Postman.exe": ["postman", "api testing"],
    "AcroRd32.exe": ["adobe reader", "pdf reader"],
    "steam.exe": ["steam", "game launcher"],
    "EpicGamesLauncher.exe": ["epic games", "epic launcher"],
    "Valorant.exe": ["valorant", "riot valorant"],
    "MinecraftLauncher.exe": ["minecraft", "minecraft launcher"],
    "WhatsApp.exe": ["whatsapp", "chat app", "messenger"],
}

def open_application(command):
    if command.startswith("open "):
        app_name = command[5:].strip().lower()  # Extract app name
        
        for exe, names in apps_dict.items():
            if app_name in names:
                print(f"Opening {exe}...")
                os.system(f"start {exe}")  # Open the application
                return
        
        print("Application not found.")
    else:
        print("Invalid command format.")

# Example Usage
while True:

    command=input("enter command: ")
    open_application(command)  
