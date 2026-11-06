# Vector Studioz — Premier Web Design Agency

This repository contains the reconstructed, high-performance agency frontend for **Vector Studioz** (`Vector Studioz — A Web Design Agency`), featuring WebGL 3D Interactive Visualization, Rive canvas animations, GSAP ScrollTriggers, and responsive design systems.

---

## Architecture Overview

1. **Frontend Core**:
   - Webflow static compilation (Site ID: `64354b8ce4872ad8cd1c7b04`)
   - Fully responsive layout with mobile/tablet breakpoints
   - Custom typography via Google WebFonts (`Inter`, `Roboto Mono`)

2. **3D WebGL Robot Visualization**:
   - Powered by Three.js `v0.151.3` + `GLTFLoader`, `RGBELoader`, `MeshoptDecoder`
   - High-fidelity GLTF 3D robot model with dynamic eye and touch video textures
   - Orthographic interactive camera with mouse-tracking and hover animations

3. **Motion & Interaction Layer**:
   - `@rive-app/canvas@2.35.0` multi-instance handler with viewport lazy-loading
   - GSAP 3.15.0 with `ScrollTrigger` for timeline coordination and animation triggers
   - Interactive slider carousels, expandable FAQs, pricing tab toggles, and ecosystem marquees

4. **Telemetry & Script Fixes**:
   - Link remapping mutation observer ensuring broken hrefs and legacy GA queries are sanitized
   - Cookie consent modal with EU GeoIP handling

---

## Running Locally

To launch a local development server:

```bash
npm run dev
# or:
npx serve -p 3000 .
```

Then visit `http://localhost:3000` in your browser.
