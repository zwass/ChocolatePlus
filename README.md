# M-Vave Chocolate Plus Control Surface for Ableton Live 12

## Overview

**Chocolate Plus** is a custom Ableton control surface script that allows your M-Vave Chocolate Plus footswitch to control clips in **Session View**.

It is **selection-aware**, meaning it always targets the **currently selected track and scene**.

No Max for Live is required. The script is **persistent across Live updates** if installed in the user Remote Scripts folder.

## Features

| Button          | CC Number | Action                                                      |
| --------------- | --------- | ----------------------------------------------------------- |
| A (short press) | 0         | Launch the clip in the **currently selected track + scene** |
| A (long press)  | 1         | Delete the clip in the **currently selected track + scene** |
| C (short press) | 4         | Select the previous **track**                                   |
| C (long press)  | 5         | Select the previous **scene**                                   |
| D (short press) | 6         | Select the next **track**                                       |
| D (long press)  | 7         | Select the next **scene**                                       |

> Additional CCs can be added to extend functionality (stop clips, scene navigation, etc.)

## Installation

### Step 1: Locate User Remote Scripts Folder (macOS)

```
~/Music/Ableton/User Library/Remote Scripts/
```

> If the folder does not exist, create it.

### Step 2: Copy the Script

Place the entire `ChocolatePlus` folder in the **Remote Scripts** folder. The structure should look like this:

```
Remote Scripts/
└── ChocolatePlus/
    ├── __init__.py
    └── ChocolatePlus.py
```

### Step 3: Configure Ableton Live

1. Open **Ableton Live 12**
2. Go to **Preferences → MIDI → Control Surface**
3. Set the control surface:

* **Control Surface:** ChocolatePlus
* **Input:** SINCO
* **Output:** None

4. Ensure **Remote = ON** for the input.

---

## M-Vave Chocolate Plus Setup

To quickly configure the footswitch the easiest method is to load the included CubeSuite preset file `Advanced custom mode.fcp`:

1. Open CubeSuite and connect your M-Vave Chocolate Plus device via USB.
2. In CubeSuite choose **Import** and select `Advanced custom mode.fcp` from the `ChocolatePlus` script folder.

---

## Usage

* **A (short press, CC 0):** Launch the clip in the **currently selected track + scene**.
* **A (long press, CC 1):** Delete the clip in the **currently selected track + scene**.
* **C (short press, CC 4):** Select the previous track.
* **C (long press, CC 5):** Select the previous scene.
* **D (short press, CC 6):** Select the next track.
* **D (long press, CC 7):** Select the next scene.

> If no clip exists in that slot, pressing delete will do nothing.

---

## Troubleshooting

1. **Control Surface does not appear in Live:**

   * Make sure the folder is in `~/Music/Ableton/User Library/Remote Scripts/Chocolate`
   * Restart Live after copying the script
   * Folder and filenames are **case-sensitive**

2. **Testing MIDI:**
   Temporarily modify `_on_launch` or `_on_delete` to show a message:

   ```python
   self.show_message(f"CC pressed!")
   ```

   Press the footswitch to confirm Live receives the message.
