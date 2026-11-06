"""
build_vector_assets.py
Generates high-fidelity dark-mode UI feature banners and case study thumbnails
for Vector Studioz with zero crypto/token references.
"""

import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('images/features', exist_ok=True)
os.makedirs('images/case-studies', exist_ok=True)

def get_fonts():
    try:
        font_h1 = ImageFont.truetype('segoeui.ttf', 32)
        font_h2 = ImageFont.truetype('segoeui.ttf', 24)
        font_body = ImageFont.truetype('segoeui.ttf', 16)
        font_pill = ImageFont.truetype('segoeui.ttf', 13)
        font_mono = ImageFont.truetype('consola.ttf', 14)
        font_mono_sm = ImageFont.truetype('consola.ttf', 12)
    except:
        font_h1 = font_h2 = font_body = font_pill = font_mono = font_mono_sm = ImageFont.load_default()
    return font_h1, font_h2, font_body, font_pill, font_mono, font_mono_sm

def draw_pill(draw, x, y, text, font, bg_color=(20, 24, 38), border_color=(45, 55, 80), text_color=(160, 185, 230)):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0] + 24
    h = bbox[3] - bbox[1] + 14
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h//2, fill=bg_color, outline=border_color, width=1)
    draw.text((x + 12, y + 6), text, font=font, fill=text_color)
    return x + w + 12

def draw_card(draw, box, fill=(15, 17, 26), border=(35, 42, 60), radius=12):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=border, width=1)

# ==============================================================================
# 1. ICL VIRTUAL SERVICES CASE STUDY THUMBNAIL (1440x810, 16:9)
# ==============================================================================
def create_iclvirtualservices_thumbnail():
    w, h = 1440, 810
    img = Image.new('RGB', (w, h), color=(9, 10, 15))
    draw = ImageDraw.Draw(img)
    f_h1, f_h2, f_body, f_pill, f_mono, f_mono_sm = get_fonts()

    # Subtle radial glow background
    for r in range(400, 0, -20):
        alpha = int(12 * (1 - r / 400))
        draw.ellipse([w//2 - r*2, h//2 - r, w//2 + r*2, h//2 + r], outline=(0, 229, 255, alpha))

    # Outer Browser Container Mockup
    draw_card(draw, [60, 50, w - 60, h - 50], fill=(13, 15, 23), border=(30, 36, 52), radius=16)

    # Top Navigation Bar
    draw_card(draw, [80, 70, w - 80, 130], fill=(18, 21, 32), border=(38, 46, 68), radius=10)
    
    # Window dots
    draw.ellipse([100, 95, 112, 107], fill=(255, 95, 86))
    draw.ellipse([120, 95, 132, 107], fill=(255, 189, 46))
    draw.ellipse([140, 95, 152, 107], fill=(39, 201, 63))

    draw.text((175, 88), "icL Virtual Services", font=f_h2, fill=(255, 255, 255))
    draw.text((420, 93), "Enterprise Remote Talent & Operational Management Engine", font=f_body, fill=(100, 116, 139))

    # Header status badge
    draw_pill(draw, w - 380, 85, "● 500+ Active Specialists", f_pill, bg_color=(0, 229, 255, 25), border_color=(0, 229, 255, 90), text_color=(0, 229, 255))
    draw_pill(draw, w - 180, 85, "99.8% SLA", f_pill, bg_color=(0, 255, 163, 25), border_color=(0, 255, 163, 90), text_color=(0, 255, 163))

    # Metric KPI Row
    kpis = [
        ("Total Verified Talent", "1,240 Specialists", "+18% this month", (0, 229, 255)),
        ("Operational Uptime", "99.94%", "Zero downtime", (0, 255, 163)),
        ("Client Timesheets Logged", "48,500 hrs", "Real-time sync", (255, 230, 0)),
        ("Placement Velocity", "< 48 Hours", "Automated pairing", (122, 0, 223))
    ]
    card_w = (w - 200) // 4
    for i, (lbl, val, sub, col) in enumerate(kpis):
        x1 = 80 + i * (card_w + 13)
        y1 = 150
        x2 = x1 + card_w
        y2 = y1 + 105
        draw_card(draw, [x1, y1, x2, y2], fill=(18, 22, 34), border=(38, 48, 70), radius=10)
        draw.text((x1 + 18, y1 + 14), lbl, font=f_pill, fill=(148, 163, 184))
        draw.text((x1 + 18, y1 + 38), val, font=f_h2, fill=(255, 255, 255))
        draw.text((x1 + 18, y1 + 74), sub, font=f_mono_sm, fill=col)

    # Left Column: Specialist Directory Card
    draw_card(draw, [80, 275, 780, h - 80], fill=(16, 19, 29), border=(35, 43, 62), radius=12)
    draw.text((105, 295), "DEPLOYED SPECIALISTS & SPRINT ROSTER", font=f_mono_sm, fill=(0, 229, 255))
    draw.text((105, 320), "Active Remote Teams & Dedicated Talent Pods", font=f_h2, fill=(255, 255, 255))

    specialists = [
        ("Amara Okafor", "Senior Next.js & React Architect", "Enterprise SaaS Pod", "Active Deployment", (0, 255, 163)),
        ("David Mensah", "Principal UI/UX & Design Systems Lead", "Fintech Client Squad", "Active Deployment", (0, 255, 163)),
        ("Fatima Al-Hassan", "Cloud DevOps & Kubernetes Engineer", "Infrastructure Pod", "Available in 48h", (0, 229, 255)),
        ("Chinedu Eze", "Full-Stack Node.js / PostgreSQL Lead", "Operations Platform", "Active Deployment", (0, 255, 163)),
        ("Zainab Bello", "QA Automation & Playwright Specialist", "Testing & CI Squad", "Active Deployment", (0, 255, 163))
    ]
    for idx, (name, role, squad, status, stat_col) in enumerate(specialists):
        sy = 370 + idx * 68
        draw_card(draw, [105, sy, 755, sy + 56], fill=(22, 26, 38), border=(40, 50, 72), radius=8)
        draw.ellipse([120, sy + 13, 150, sy + 43], fill=(35, 45, 68), outline=(0, 229, 255))
        draw.text((127, sy + 18), name[:2].upper(), font=f_pill, fill=(0, 229, 255))
        draw.text((165, sy + 10), name, font=f_body, fill=(255, 255, 255))
        draw.text((165, sy + 32), f"{role} • {squad}", font=f_mono_sm, fill=(148, 163, 184))
        draw_pill(draw, 600, sy + 14, status, f_mono_sm, bg_color=(15, 20, 30), border_color=stat_col, text_color=stat_col)

    # Right Column: Operational Telemetry & Analytics
    draw_card(draw, [805, 275, w - 80, h - 80], fill=(16, 19, 29), border=(35, 43, 62), radius=12)
    draw.text((830, 295), "SYSTEM TELEMETRY & PRODUCTIVITY METRICS", font=f_mono_sm, fill=(122, 0, 223))
    draw.text((830, 320), "Weekly Concurrency & Sprint Hours", font=f_h2, fill=(255, 255, 255))

    # Graph Area
    gx1, gy1, gx2, gy2 = 830, 380, w - 105, 590
    draw_card(draw, [gx1, gy1, gx2, gy2], fill=(20, 24, 36), border=(38, 48, 70), radius=8)
    
    # Grid lines
    for line_y in range(gy1 + 30, gy2, 45):
        draw.line([gx1 + 10, line_y, gx2 - 10, line_y], fill=(32, 40, 58), width=1)
    
    # Glowing chart path
    points = [
        (gx1 + 30, gy2 - 40), (gx1 + 90, gy2 - 65), (gx1 + 160, gy2 - 50),
        (gx1 + 230, gy2 - 110), (gx1 + 300, gy2 - 95), (gx1 + 370, gy2 - 140),
        (gx1 + 440, gy2 - 165), (gx2 - 40, gy2 - 180)
    ]
    for pi in range(len(points) - 1):
        draw.line([points[pi], points[pi+1]], fill=(0, 229, 255), width=3)
        draw.ellipse([points[pi][0]-4, points[pi][1]-4, points[pi][0]+4, points[pi][1]+4], fill=(0, 255, 163))
    draw.ellipse([points[-1][0]-5, points[-1][1]-5, points[-1][0]+5, points[-1][1]+5], fill=(255, 255, 255), outline=(0, 229, 255), width=2)

    draw.text((gx1 + 20, gy1 + 12), "Peak Velocity: 3,420 SP / Sprint", font=f_mono_sm, fill=(0, 229, 255))
    draw.text((gx2 - 180, gy1 + 12), "● Live Production Data", font=f_mono_sm, fill=(0, 255, 163))

    # Watermark Pill
    draw_pill(draw, 830, 620, "CLIENT SHOWCASE // VECTOR STUDIOZ FULL-STACK BUILD", f_mono, bg_color=(0, 229, 255, 20), border_color=(0, 229, 255, 80), text_color=(0, 229, 255))
    draw.text((830, 670), "Engineered with Next.js 14 App Router, PostgreSQL, Prisma, and Cloudflare CDN.", font=f_body, fill=(148, 163, 184))

    out_path = 'images/case-studies/iclvirtualservices.png'
    img.save(out_path, format='PNG', quality=95)
    print(f"Generated {out_path} ({w}x{h})")

# ==============================================================================
# 2. FEATURE BANNER HELPER (1200x800)
# ==============================================================================
def create_feature_banner(filename, badge_text, headline_text, pills, left_title, left_lines, right_title, right_data, accent_color=(0, 229, 255)):
    w, h = 1200, 800
    img = Image.new('RGB', (w, h), color=(10, 11, 16))
    draw = ImageDraw.Draw(img)
    f_h1, f_h2, f_body, f_pill, f_mono, f_mono_sm = get_fonts()

    # Outer Container Glass Card
    draw_card(draw, [30, 30, w - 30, h - 30], fill=(13, 15, 22), border=(30, 36, 52), radius=16)

    # Top Pill Chips
    px = 60
    for ptext in pills:
        px = draw_pill(draw, px, 55, ptext, f_pill, bg_color=(20, 24, 38), border_color=(45, 55, 80), text_color=(200, 215, 240))

    # Banner Header
    draw.text((60, 115), badge_text.upper(), font=f_mono_sm, fill=accent_color)
    draw.text((60, 138), headline_text, font=f_h1, fill=(255, 255, 255))

    # Two Main Panels
    panel_w = (w - 150) // 2
    
    # Left Panel
    draw_card(draw, [60, 205, 60 + panel_w, h - 140], fill=(17, 20, 30), border=(36, 44, 64), radius=12)
    draw.text((85, 225), left_title.upper(), font=f_mono_sm, fill=accent_color)
    for l_idx, line in enumerate(left_lines):
        draw.text((85, 260 + l_idx * 32), line, font=f_mono, fill=(210, 225, 245) if ':' not in line else (160, 180, 210))

    # Right Panel
    draw_card(draw, [90 + panel_w, 205, w - 60, h - 140], fill=(17, 20, 30), border=(36, 44, 64), radius=12)
    draw.text((115 + panel_w, 225), right_title.upper(), font=f_mono_sm, fill=(0, 255, 163))
    for r_idx, (r_label, r_val, r_sub) in enumerate(right_data):
        ry = 265 + r_idx * 75
        draw_card(draw, [115 + panel_w, ry, w - 85, ry + 62], fill=(22, 26, 38), border=(38, 48, 70), radius=8)
        draw.text((135 + panel_w, ry + 10), r_label, font=f_pill, fill=(148, 163, 184))
        draw.text((135 + panel_w, ry + 32), r_val, font=f_h2, fill=(255, 255, 255))
        draw.text((w - 240, ry + 32), r_sub, font=f_mono_sm, fill=accent_color)

    # Bottom Studio Action Strip (mimicking Webflow input mockup with zero crypto)
    draw_card(draw, [60, h - 120, w - 60, h - 55], fill=(18, 22, 34), border=(40, 50, 75), radius=10)
    draw.text((90, h - 96), "Vector Studioz Production Architecture • Verified Performance Standards", font=f_body, fill=(160, 175, 205))
    draw_pill(draw, w - 260, h - 105, "ENTERPRISE READY", f_mono_sm, bg_color=(0, 229, 255, 20), border_color=(0, 229, 255, 90), text_color=(0, 229, 255))

    out_path = os.path.join('images/features', filename)
    img.save(out_path, format='PNG', quality=95)
    print(f"Generated {out_path} ({w}x{h})")

# Generate all 6 feature banners
def build_all_features():
    # 1. Design System
    create_feature_banner(
        filename='vector-design-system.png',
        badge_text="Figma Multi-Tier Architecture",
        headline_text="Atomic Design Tokens & Micro-Interactions",
        pills=["Design Tokens", "Typography Scale", "Atomic Components", "Micro-Interactions", "WCAG 2.1 AA"],
        left_title="Token Variables & Theme Config",
        left_lines=[
            "const themeTokens = {",
            "  colors: {",
            "    cyan: '#00e5ff',",
            "    purple: '#7a00df',",
            "    surfaceDark: '#08090c',",
            "    glassBorder: 'rgba(255,255,255,0.08)'",
            "  },",
            "  radii: { sm: '6px', md: '12px', full: '9999px' },",
            "  physics: { springStiffness: 320, damping: 28 }",
            "};"
        ],
        right_title="Design System Performance",
        right_data=[
            ("Component Coverage", "148 Reusable Units", "100% Typed"),
            ("Lighthouse Accessibility", "Score: 100/100", "Zero Contrast Flags"),
            ("Handoff Velocity", "3x Faster to Code", "Figma Variables")
        ],
        accent_color=(0, 229, 255)
    )

    # 2. 3D & WebGL Shader
    create_feature_banner(
        filename='vector-webgl-shader.png',
        badge_text="Three.js & Hardware Shaders",
        headline_text="Interactive 3D WebGL Spatial Canvases",
        pills=["Three.js 60fps", "GLSL Shaders", "Draco Mesh -78%", "PBR Reflections", "Touch Kinetics"],
        left_title="Custom Fragment Shader (GLSL)",
        left_lines=[
            "precision highp float;",
            "uniform float u_time;",
            "uniform vec2 u_resolution;",
            "varying vec2 vUv;",
            "void main() {",
            "  vec2 p = -1.0 + 2.0 * vUv;",
            "  float len = length(p);",
            "  vec3 col = vec3(0.0, 0.9, 1.0) / len;",
            "  gl_FragColor = vec4(col * abs(sin(u_time)), 1.0);",
            "}"
        ],
        right_title="WebGL Engine Metrics",
        right_data=[
            ("Framerate Stability", "60.0 FPS Stable", "16.6ms / frame"),
            ("Geometry Draco Compression", "1.4 MB Total", "-78% Bandwidth"),
            ("Draw Calls per Frame", "14 Draw Calls", "GPU Hardware Accel")
        ],
        accent_color=(0, 255, 163)
    )

    # 3. Full-Stack Telemetry
    create_feature_banner(
        filename='vector-fullstack-telemetry.png',
        badge_text="Next.js 14 & Edge Compute",
        headline_text="Full-Stack Edge Latency & Streaming SSR",
        pills=["Next.js 14", "App Router", "Sub-Second Edge", "Strict TypeScript", "Automated CI/CD"],
        left_title="Edge Server Component Pipeline",
        left_lines=[
            "export async function EdgeDataPipeline() {",
            "  const res = await fetch(API_EDGE_ENDPOINT, {",
            "    next: { revalidate: 60 },",
            "    headers: { 'x-edge-cache': 'hit' }",
            "  });",
            "  const data: VerifiedSchema = await res.json();",
            "  return <StreamingView payload={data} />;",
            "}"
        ],
        right_title="Edge Concurrency & Latency",
        right_data=[
            ("Global TTFB (Time to First Byte)", "38 ms Global Avg", "Cloudflare Edge"),
            ("Lighthouse Overall Score", "99 / 100", "Top 1% Tier"),
            ("Concurrent Load Capacity", "50,000 req/sec", "Zero Failures")
        ],
        accent_color=(0, 229, 255)
    )

    # 4. Cloud Architecture
    create_feature_banner(
        filename='vector-cloud-architecture.png',
        badge_text="Distributed Systems & IaC",
        headline_text="Resilient Cloud Microservices & High-Throughput",
        pills=["Microservices", "Kafka Queues", "Zero Downtime", "Terraform IaC", "PostgreSQL Shards"],
        left_title="Infrastructure as Code (Terraform)",
        left_lines=[
            "resource 'aws_ecs_service' 'api_gateway' {",
            "  name            = 'vector-edge-cluster'",
            "  desired_count   = 16",
            "  launch_type     = 'FARGATE'",
            "  deployment_controller {",
            "    type = 'CODE_DEPLOY_BLUE_GREEN'",
            "  }",
            "  health_check_grace_period_seconds = 15",
            "}"
        ],
        right_title="Cloud Availability & SLA",
        right_data=[
            ("Production Availability", "99.99% Uptime", "Multi-Region VPC"),
            ("Event Stream Processing", "120,000 msg/sec", "Kafka Clusters"),
            ("Deployment Failover", "0.00s Zero Downtime", "Blue/Green Cutover")
        ],
        accent_color=(122, 0, 223)
    )

    # 5. AI Multi-Agent Swarms
    create_feature_banner(
        filename='vector-ai-agents.png',
        badge_text="Autonomous AI & RAG Workflows",
        headline_text="Enterprise Multi-Agent Orchestration Graphs",
        pills=["LangGraph State", "Hybrid RAG Index", "Zero Data Retention", "Citation Checks", "Tool Calling"],
        left_title="Multi-Agent Coordination Graph",
        left_lines=[
            "const workflow = new StateGraph({",
            "  nodes: {",
            "    researcher: searchVectorStore,",
            "    verifier: verifySourceCitations,",
            "    executor: executeAutomatedTool",
            "  },",
            "  entryPoint: 'researcher',",
            "  edges: [['researcher', 'verifier'], ['verifier', 'executor']]",
            "});"
        ],
        right_title="AI Pipeline Reliability",
        right_data=[
            ("Hallucination Rejection Rate", "99.7% Accuracy", "RAG Evaluation"),
            ("Inference Response Time", "0.85s Latency", "Streaming Tokens"),
            ("Data Privacy Guarantee", "0% Retention", "Private VPC Nodes")
        ],
        accent_color=(0, 229, 255)
    )

    # 6. Mobile App Kinetics
    create_feature_banner(
        filename='vector-mobile-apps.png',
        badge_text="Cross-Platform Mobile",
        headline_text="Native 120Hz Gestures & Offline Data Sync",
        pills=["Flutter / React Native", "120Hz ProMotion", "Offline SQLite Sync", "Fastlane CI/CD", "Biometrics"],
        left_title="Fluid Gesture Controller",
        left_lines=[
            "class FluidSheetController extends State {",
            "  late final AnimationController _kinetics;",
            "  void onSwipe(DragUpdateDetails details) {",
            "    _kinetics.animateWith(SpringSimulation(",
            "      SpringDescription(mass: 1.0, stiffness: 350.0, damping: 25.0),",
            "      0.0, 1.0, details.primaryVelocity ?? 0.0",
            "    ));",
            "  }",
            "}"
        ],
        right_title="Native Device Performance",
        right_data=[
            ("Frame Drop Rate", "0.02% (Silky)", "120Hz ProMotion"),
            ("Offline Storage Engine", "SQLite + Realm", "Bi-directional Sync"),
            ("App Store Approval Rate", "100% First-Pass", "Strict Compliance")
        ],
        accent_color=(0, 255, 163)
    )

if __name__ == '__main__':
    create_iclvirtualservices_thumbnail()
    build_all_features()
    print("All Vector Studioz visual assets generated successfully!")

