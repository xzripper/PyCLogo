# PyCLogo (Python (Means that was made on Python) Console Logo) - Simple but powerful re-make of neofetch.
PyCLogo is a simple but powerful re-make of neofetch.
Allows you to create similar to neofetch windows.

Console:<br><img src="PyCLogo\PyCLogoExample.png">

Code:<br>
```python
from pyclogo import PyCLogo


logo = PyCLogo()

logo.update_image("icon.png")

logo.add_info("Project", "PyCLogo.")
logo.add_info("Description.", "PyCLogo is simple but powerful re-make of neofetch that allows you print beautiful info windows.")
logo.add_info("Author.", "Ivan Perzhynsky.")
logo.add_info("Version", "1.0")
logo.add_info("License", "MIT License.")
logo.add_info("Note", "I don't know why logo is Arch Linux...")
logo.add_info("Key", "Value.")

logo.print_window("blue")

```

## Installation.
Download ZIP code.<br>
Un-pack ```PyCLogo``` to ```PYTHON_PATH\Lib```.<br>
Open un-packed folder in terminal.<br>
Write ```pip install -r pyclogo_req.txt```.<br>
Done!
