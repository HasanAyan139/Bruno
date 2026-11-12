import psutil
target_processes = [
    "Lively.exe",
    "copilotapp.exe",
    "copilotapphost.exe",
    "copilot-runtime.exe",
    "WhatsApp.Root.exe",
    "steam.exe",
    "steamwebhelper.exe",
    "Discord.exe",
    "EpicGamesLauncher.exe",
    "EpicWebHelper.exe",
    "ChatGPT.exe",
    "RiotClientServices.exe"
]
success_count = 0
timeout_count = 0
not_found_count = 0
access_denied_count = 0
for process in psutil.process_iter():
    try:
        name = process.name()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

    if name in target_processes:
        try:
            print(f"{name} bulundu: PID {process.pid}")
            process.terminate()
            process.wait(timeout=3)
            success_count += 1
            print(f"{name} kapatıldı.")

        except psutil.TimeoutExpired:
            print(f"{name} zamanında kapanamadı.")
            timeout_count += 1

        except psutil.NoSuchProcess:
            print(f"{name} zaten kapanmış.")
            not_found_count += 1

        except psutil.AccessDenied:
            print(f"{name} için erişim reddedildi.")
            access_denied_count += 1

print(f"\nToplam başarıyla kapatılan süreçler: {success_count}")
print(f"Zamanında kapanamayan süreçler: {timeout_count}")
print(f"Zaten kapanmış süreçler: {not_found_count}")
print(f"Erişim reddedilen süreçler: {access_denied_count}")