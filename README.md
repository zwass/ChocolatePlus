# M-Vave Chocolate Plus Control Surface for Ableton Live 12

## Overview

**Chocolate Plus** is a custom Ableton control surface script that allows your M-Vave Chocolate Plus footswitch to control clips in **Session View**.

It is **selection-aware**, meaning it targets the **currently selected track and scene**.

No Max for Live is required.

## Features

| Button          | CC Number | Action                                                      |
| --------------- | --------- | ----------------------------------------------------------- |
| **A (short press)** | 0         | Launch the clip in the **currently selected track + scene** |
| **A (long press)**  | 1         | Delete the clip in the **currently selected track + scene** |
| **C (short press)** | 4         | Select the previous **track**                                   |
| **C (long press)**  | 5         | Select the previous **scene**                                   |
| **D (short press)** | 6         | Select the next **track**                                       |
| **D (long press)**  | 7         | Select the next **scene**                                       |

> The **B** button is not yet configured. It can be MIDI-mapped as desired. If you have an idea of how to best use this button, please [file an issue on GitHub](https://github.com/zwass/ChocolatePlus/issues/new).

## Installation

### Step 1: Locate User Remote Scripts Folder

**macOS:**
```
~/Music/Ableton/User Library/Remote Scripts/
```

**Windows:**
```
%USERPROFILE%\Documents\Ableton\User Library\Remote Scripts\
```

> If the `Remote Scripts` folder does not exist, create it.

### Step 2: Get the Script

Choose one of the following methods:

**Option A: Clone from GitHub**
```bash
cd /path/to/Remote\ Scripts/
git clone https://github.com/zwass/ChocolatePlus.git
```

Now future updates can easily be retrieved with `git pull`.

**Option B: Download the ZIP file**
1. Download the [latest version](https://github.com/zwass/ChocolatePlus/archive/refs/heads/main.zip) from GitHub
2. Extract the ZIP file
3. Move the `ChocolatePlus` folder to your `Remote Scripts` folder

Either method will result in this structure:
```
Remote Scripts/
└── ChocolatePlus/
    ├── __init__.py
    └── ChocolatePlus.py
```

### Step 3: Configure Ableton Live

1. Restart **Ableton Live** (necessary for Live to pick up the new Control Surface)
2. Go to **Preferences → MIDI → Control Surface**
3. Set the Control Surface:

* **Control Surface:** ChocolatePlus
* **Input:** SINCO
* **Output:** None

4. Ensure **Remote = ON** for the input.

## M-Vave Chocolate Plus Setup

To quickly configure the footswitch the easiest method is to load the included CubeSuite preset file `Advanced custom mode.fcp`:

1. Open CubeSuite and connect your M-Vave Chocolate Plus device via USB.
2. In CubeSuite choose **Import** and select `Advanced custom mode.fcp` from the `ChocolatePlus` script folder.

Importing the preset file will allow you to see and modify the configurations if you would like to make changes.

## Usage

* **A (short press, CC 0):** Launch the clip in the **currently selected track + scene**.
* **A (long press, CC 1):** Delete the clip in the **currently selected track + scene**.
* **C (short press, CC 4):** Select the previous track.
* **C (long press, CC 5):** Select the previous scene.
* **D (short press, CC 6):** Select the next track.
* **D (long press, CC 7):** Select the next scene.

> If no clip exists in that slot, pressing delete will do nothing.

## Troubleshooting

### Control Surface does not appear in Live settings:

   * Make sure the `ChocolatePlus` folder is in the `Remote Scripts` folder of the User Library
   * Restart Live after installation
   * Folder and filenames are **case-sensitive**

### Debugging MIDI
1. Set Control Surface to **None** in **Preferences → MIDI → Control Surface**
2. Create a MIDI track and insert the **MIDI Monitor** MIDI Effect before any other devices. Select **Flow** and then press buttons on the foot switch to see the messages that are received by Live. These should be **CTL** values corresponding to those documented in this README.
3. Set the Control Surface back to **ChocolatePlus**

