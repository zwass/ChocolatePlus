from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.ButtonElement import ButtonElement

class ChocolatePlus(ControlSurface):

    def __init__(self, c_instance):
        super().__init__(c_instance)

        with self.component_guard():
            self._setup_buttons()

    def _setup_buttons(self):
        # CC 0 → Launch clip
        self.launch_button = ButtonElement(
            True,           # momentary
            MIDI_CC_TYPE,
            0,              # Channel 1
            0              # CC 0
        )
        self.launch_button.add_value_listener(self._on_launch)

        # CC 1 → Delete clip
        self.delete_button = ButtonElement(
            True,           # momentary
            MIDI_CC_TYPE,
            0,              # Channel 1
            1              # CC 1
        )
        self.delete_button.add_value_listener(self._on_delete)

    # ===== Launch clip =====
    def _on_launch(self, value):
        if value == 0:
            return

        song = self.song()
        view = song.view

        track = view.selected_track
        scene = view.selected_scene

        if not track or not scene:
            return

        try:
            scene_index = list(song.scenes).index(scene)
            clip_slot = track.clip_slots[scene_index]
            clip_slot.fire()
        except Exception:
            pass

    # ===== Delete clip =====
    def _on_delete(self, value):
        if value == 0:
            return

        song = self.song()
        view = song.view

        track = view.selected_track
        scene = view.selected_scene

        if not track or not scene:
            return

        try:
            scene_index = list(song.scenes).index(scene)
            clip_slot = track.clip_slots[scene_index]
            if clip_slot.has_clip:
                clip_slot.delete_clip()
        except Exception:
            pass
