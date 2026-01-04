from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.ButtonElement import ButtonElement

class ChocolatePlus(ControlSurface):
    def __init__(self, c_instance):
        super().__init__(c_instance)

        with self.component_guard():
            self._setup_buttons()

    def _create_button(self, cc, callback):
        """Helper to create a momentary CC button and attach its listener."""
        btn = ButtonElement(True, MIDI_CC_TYPE, 0, cc)
        btn.add_value_listener(callback)
        return btn

    def _change_selection(self, items, current, offset):
        """Return the item offset from current with wraparound, or None if invalid."""
        if not items:
            return None
        try:
            idx = items.index(current)
        except Exception:
            return None
        return items[(idx + offset) % len(items)]

    def _setup_buttons(self):
        # CC 0 → Launch clip
        self.launch_button = self._create_button(0, self._on_launch)

        # CC 1 → Delete clip
        self.delete_button = self._create_button(1, self._on_delete)

        # CC 4 → Previous track
        self.prev_button = self._create_button(4, self._on_prev_track)

        # CC 5 → Previous scene
        self.prev_scene_button = self._create_button(5, self._on_prev_scene)

        # CC 6 → Next track
        self.next_button = self._create_button(6, self._on_next_track)

        # CC 7 → Next scene
        self.next_scene_button = self._create_button(7, self._on_next_scene)

    # ===== Launch clip =====
    def _on_launch(self, value):
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

    # ===== Next track =====
    def _on_next_track(self, value):
        song = self.song()
        view = song.view
        target = self._change_selection(list(song.tracks), view.selected_track, 1)
        if target:
            view.selected_track = target

    # ===== Previous track =====
    def _on_prev_track(self, value):
        song = self.song()
        view = song.view
        target = self._change_selection(list(song.tracks), view.selected_track, -1)
        if target:
            view.selected_track = target

    # ===== Next scene =====
    def _on_next_scene(self, value):
        song = self.song()
        view = song.view
        target = self._change_selection(list(song.scenes), view.selected_scene, 1)
        if target:
            view.selected_scene = target

    # ===== Previous scene =====
    def _on_prev_scene(self, value):
        song = self.song()
        view = song.view
        target = self._change_selection(list(song.scenes), view.selected_scene, -1)
        if target:
            view.selected_scene = target
