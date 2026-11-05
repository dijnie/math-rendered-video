# 3D Scenes & Moving Camera

## ThreeDScene basics

```python
class Surf(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: axes.c2p(u, v, np.sin(u) * np.cos(v)),
            u_range=[-3, 3], v_range=[-3, 3],
            resolution=(30, 30),
        )
        surface.set_style(fill_opacity=0.7)
        self.add(axes)
        self.play(Create(surface))
        self.wait()
```

- `set_camera_orientation(phi=, theta=, zoom=, focal_distance=)` — `phi` tilts from the z-axis, `theta` spins around it. Use `DEGREES`.
- `ThreeDAxes`, `Sphere`, `Cube`, `Prism`, `Surface` (parametric via `c2p`), `ParametricFunction` for 3D curves.
- `resolution=(n, m)` controls Surface mesh density (higher = smoother but slower).

## Ambient + animated camera (3D)

```python
self.begin_ambient_camera_rotation(rate=0.2)   # slow continuous orbit
self.wait(5)
self.stop_ambient_camera_rotation()

# or animate camera explicitly
self.move_camera(phi=45 * DEGREES, theta=30 * DEGREES, run_time=3)
```

`add_fixed_in_frame_mobjects(label)` keeps a 2D label (title, caption) pinned to the screen instead of floating in 3D space.

## Moving camera (2D)

`MovingCameraScene` exposes `self.camera.frame` as an animatable mobject — push in, pan, follow.

```python
class Follow(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        dot = Dot()
        self.add(dot)
        # zoom in and recenter on the dot
        self.play(self.camera.frame.animate.scale(0.5).move_to(dot))
        # follow a moving dot with an updater
        self.camera.frame.add_updater(lambda f: f.move_to(dot))
        self.play(dot.animate.shift(RIGHT * 4))
        self.camera.frame.clear_updaters()
        self.play(Restore(self.camera.frame))   # back to the saved full view
```

- `self.camera.frame.animate.scale(0.5)` zooms in (smaller frame = closer); `.move_to(x)` pans.
- `save_state()` / `Restore(self.camera.frame)` — snapshot and return to a framing.
- Follow a target by adding an updater that moves the frame to it each frame; `clear_updaters()` to release.

## Tips

- 3D renders are slower — iterate with `-ql` and a low Surface `resolution`, raise both only for the final `-qh` encode.
- Verify a 3D shot with `manim -sql ... -n a,b` (save a frame) to check the camera angle and that nothing is behind the camera before the full render.
- Keep ambient rotation slow (`rate` ~0.1–0.3); fast orbits read as disorienting, not explanatory.


## Camera language — which angle for what

| Shot | 2D (`MovingCameraScene`) | 3D (`ThreeDScene`) | Use |
|---|---|---|---|
| Establishing / wide | full frame | `phi=65°, theta=-45°` (or `-60°`), `zoom=0.8` | introduce the whole object |
| Push-in | `frame.animate.scale(0.5).move_to(obj)` | `move_camera(zoom=1.6, frame_center=obj)` | "now look at this detail" |
| Pull-out / reveal | `Restore(frame)` after `save_state()` | `move_camera(zoom=0.7)` | the detail is part of something bigger |
| Pan / follow | `frame.add_updater(lambda f: f.move_to(dot))` | `move_camera(frame_center=…)` | follow a moving point |
| Top-down | — | `phi=0, theta=-90°` | 3D object seen as a 2D map (contours, regions) |
| Side / profile | — | `phi=90°, theta=-90°` | height of a surface, a cross-section |
| Low angle | — | `phi=80–85°` | make an object feel large |
| Orbit | — | `begin_ambient_camera_rotation(rate=0.15)` | show 3D shape is 3D; while the voice explains |
| Wobble | — | `begin_3dillusion_camera_rotation(rate=1)` | subtle "it's 3D" movement on a near-static shot |
| Detail inset | `ZoomedScene` (`self.activate_zooming(animate=True)`, move `self.zoomed_camera.frame`) | — | magnifier on a tiny region while keeping the whole |

Rules:
- One camera move per idea; hold still while equations are being read.
- Camera moves are slower than object moves: 2–4 s, `rate_func=smooth` (or `double_smooth`).
- Avoid `phi=0` straight-down views of surfaces (they flatten); avoid theta near 0° or 90° (axes overlap).
- Pin titles, equations and readouts with `add_fixed_in_frame_mobjects` (3D) — in `MovingCameraScene` a fixed overlay needs to be re-positioned relative to `frame` with an updater, or kept in a separate scene.

## 3D look

- Surfaces: `surface.set_fill_by_value(axes=axes, colorscale=[(A2, -1), (ACCENT, 1)], axis=2)` colours by height; `surface.set_fill_by_checkerboard(A2, ACCENT, opacity=0.6)` for a classic grid look; `set_style(fill_opacity=0.7, stroke_width=0.5, stroke_color=MUTED)`.
- Light: `self.camera.light_source.move_to(5 * LEFT + 5 * OUT)` moves the shading light; the effect is subtle, so rely on colour scales more than lighting.
- `add_fixed_orientation_mobjects(label)` keeps a label facing the camera but still placed in 3D.
- Keep 3D axes quiet (`ThreeDAxes(axis_config={"color": MUTED})`) and add labels with `axes.get_axis_labels(...)`.
