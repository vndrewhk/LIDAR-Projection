import subprocess

btn_overlay_process = subprocess.Popen(["python", "btn_overlay.py"])
mouse_mover_process = subprocess.Popen(["python", "mouse_mover.py"])

btn_overlay_process.wait()
mouse_mover_process.wait()

# Subprocess is used to launch both Python scripts simultaneously. Multithreading is not
# necessary here because the two programs do not need to share the same memory space.