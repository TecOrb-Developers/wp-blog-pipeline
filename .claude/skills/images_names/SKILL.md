---
name: images-names
description: Predefined image library for Tecorb blog posts. Contains the full catalog of 30 available hero images (1280×720) organized by technology category. Use this skill to select the featured image for every blog post. Consult this skill before writing the manifest.json for any draft. Do not use AI image generation — all blog visuals come from this library.
metadata:
  type: reference
---

# Image Library — Tecorb Blog Predefined Images

All blog post visuals are selected from this library. No AI image generation is used. This skill defines the catalog, folder location, naming conventions, and selection workflow.

---

## 1. Folder location

```
drafts/images_to_use/images/pre_images/
└── AI_Blog_1280_720/    ← hero / featured images (the only folder used)
```

The hero images live under `drafts/images_to_use/images/pre_images/AI_Blog_1280_720/` relative to the project root.

---

## 2. Per-blog image rule

Every blog post includes exactly:

| Role | Folder | Count |
|---|---|---|
| **Hero / featured image** | `AI_Blog_1280_720` | 1 |

The hero image is set as the WordPress featured image. No in-body images are used in the current pipeline.

---

## 3. Naming convention

| Variant | Naming pattern | Example |
|---|---|---|
| 1280×720 hero | `{N}. {Title}_Hero_Page.png` | `1. Custom LLM & SLM Development_Hero_Page.png` |

Some images in the library do not have the `_Hero_Page` suffix — use the exact filename as listed in Section 6.

---

## 4. Selection workflow

1. Read the blog draft and identify the primary topic and technology focus
2. Scan the Summary Reference Table (Section 7) to find images whose category and key technologies match the blog
3. Read the **Image about** description for the top 1-2 candidates to confirm thematic fit
4. Select **1 image** from `AI_Blog_1280_720` for the hero
5. Verify the file exists at `drafts/images_to_use/images/pre_images/AI_Blog_1280_720/<filename>`
6. Record the selection in `images/manifest.json` with alt text

---

## 5. Selection criteria

- **Topic match** — The image's category and key technologies should align with the blog's primary subject (e.g., an LLM fine-tuning post → Image 02)
- **Best single match** — When in doubt, prefer the image whose description most closely mirrors the blog's central concept

When the blog topic does not match any single image exactly, pick the closest thematic match. A post about monitoring in AWS fits Image 29 (Cloud Monitoring) even if it doesn't cover every listed tool.

---

## 6. Full image catalog

---

## AI & Machine Learning

---

### Image 01 — Custom LLM & SLM Development
Size 1280 × 720, Name= 1. Custom LLM & SLM Development_Hero_Page.png

**Image about:**
A photorealistic, cinematic wide-angle illustration of a neural network being constructed inside a glowing holographic workspace. Floating 3D nodes pulse with electric-blue and deep-violet light, connected by luminous synaptic threads that form the shape of a brain blending into a microchip. A sleek developer's workstation is visible in the foreground — multiple monitors display Python code and loss-curve graphs. The environment feels like a high-tech innovation lab: dark background, dramatic lighting, subtle lens flare. Text overlays are absent. The mood is futuristic, intelligent, and aspirational — conveying that a bespoke large language model is being engineered from the ground up by expert hands.

---

### Image 02 — Fine-Tuning Open-Weight LLMs & Small Language Models

Size 1280 × 720, Name= 2. Fine-Tuning Open-Weight LLMs & Small Language Models_Hero_Page.png

**Image about:**
A sleek, flat-style isometric 3D illustration showing a large language model represented as a giant glowing cube being sculpted and refined by robotic precision tools. Sparks of golden light fly off as layers are carved away, revealing a smaller, denser, faster core — like a sculptor revealing a diamond inside a rough stone. Around it float data cards labeled with domain-specific icons: medical, legal, finance, retail. The colour palette is deep indigo, electric blue, and gold. The background is a dark navy grid, suggesting a technical environment. The overall feeling is precision engineering meets AI intelligence — a model tailored perfectly for a specific business purpose.

---

### Image 03 — Reinforcement Learning (RLHF, DPO, GRPO, DQN)
Size 1280 × 720, Name= 3. Reinforcement Learning (RLHF, DPO, GRPO, DQN)_Hero_Page.png

**Image about:**
A dynamic, high-detail digital artwork of an AI agent navigating a complex 3D labyrinth of glowing pathways. At each decision fork, reward signals appear as bursts of green light while incorrect paths fade into red. Above the maze, a holographic reward graph curves upward — showing learning over time. In the background, abstract representations of human feedback appear as silhouettes giving thumbs-up signals that feed into the model's reward function. The style is semi-realistic with a cinematic quality. Colours: emerald green, signal red, deep charcoal. The concept communicates: intelligent systems learning from experience, human guidance, and trial-and-error to continuously improve behaviour.

---

### Image 04 — LLM Harness & Orchestration
Size 1280 × 720, Name= 4. LLM Harness & Orchestration_Hero_Page.png

**Image about:**
A bird's-eye-view technical diagram rendered as a beautiful 3D isometric illustration. Multiple AI models are depicted as glowing server nodes, each specialised — one for vision, one for language, one for reasoning. They are connected by animated pipelines flowing into a central orchestration hub shaped like a conductor's podium. Data streams visualised as coloured ribbons (teal, amber, violet) flow between the nodes in perfect synchrony. The whole system sits on a transparent glass platform above a city skyline, suggesting enterprise scale. The aesthetic is clean, modern, and professional — communicating seamless multi-model coordination powered by robust engineering.

---

### Image 05 — AI Agents: OpenClaw, NanoClaw, Hermes

Size 1280 × 720, Name= 5. AI Agents_ OpenClaw, NanoClaw, Hermes_Hero_Page.png

**Image about:**
Three distinct AI agents depicted as sleek robotic figures with unique visual identities, standing together in a futuristic command centre. The first is large and powerful (OpenClaw) — a heavy-duty robot with claw-like manipulators processing complex data streams. The second is compact and nimble (NanoClaw) — a small, lightning-fast unit embedded in a mobile device interface. The third is a winged messenger figure (Hermes) — agile and communicative, routing information between systems. All three glow with the same brand-blue core. Behind them, a panoramic display shows real-time task completion metrics. The style is concept-art quality, cinematic, and technically detailed — conveying autonomous AI agents built for real business workflows.

---

### Image 06 — MLOps: MLflow, W&B, Kubeflow, SageMaker, Prefect

Size 1280 × 720, Name= 6. MLOps_ MLflow, W&B, Kubeflow, SageMaker, Prefect_Hero_Page.png

**Image about:**
A wide, clean infographic-style illustration of an end-to-end machine learning pipeline running like a production assembly line. Each stage is a glowing module on a conveyor belt: Data Ingestion → Experiment Tracking → Model Training → Evaluation → Deployment → Monitoring. Each module displays a stylised logo representation and floating metric cards (accuracy, latency, drift score). The art style is flat 2.5D with deep blue and teal tones, accented by orange for alert states. The image conveys operational maturity and engineering discipline — an ML lifecycle managed with professional-grade tooling, not ad hoc scripts.

---

### Image 07 — Vector Databases (Pinecone, PGVector, FAISS, Chroma, MongoDB Atlas)

Size 1280 × 720, Name= 7. Vector Databases (Pinecone, PGVector, FAISS, Chroma, MongoDB Atlas).png

**Image about:**
A visually rich abstract illustration of semantic search in action. Hundreds of glowing data orbs of different colours float in 3D space — each orb represents a document, image, or text chunk embedded as a vector. A search query, visualised as a bright pulsing beam, enters the space and magnetically attracts the most similar orbs — pulling them forward in a cluster. The background is dark with a subtle grid, like looking inside a high-dimensional embedding space. Distance lines between similar items are rendered as faint dotted arcs. The colour palette: deep purple, electric teal, warm amber. The concept communicates: AI-powered similarity search at massive scale — fast, accurate, intelligent retrieval.

---

### Image 08 — LangChain, LangFlow & LlamaIndex

Size 1280 × 720, Name= 8. LangChain, LangFlow & LlamaIndex.png

**Image about:**
A colourful, well-structured flowchart illustration rendered in an isometric 3D style. A prompt enters the system on the left, passes through a retrieval stage (documents being searched), then a reasoning chain (interconnected thought bubbles processing logic), and finally exits as a polished AI response on the right. Each component is a floating block in a chain — glowing connectors visualise the data flow. Stylised icons for document loaders, memory buffers, and tool calls are embedded in each block. The art style is modern SaaS product illustration quality. The image communicates: building powerful AI pipelines by connecting modular components — no black box, just transparent, composable AI engineering.

---

### Image 09 — Llama.cpp & vLLM Deployment

Size 1280 × 720, Name= 9. Llama.cpp & vLLM Deployment.png

**Image about:**
A dramatic, cinematic illustration of a high-performance AI inference engine running at full speed. Visualised as a Formula 1 race car (shaped like a server rack) blazing down a data highway. The car's chassis is etched with neural network diagrams; the exhaust trails are streams of processed tokens. Surrounding it are benchmark indicators — tokens per second, latency meters, GPU temperature gauges — all in the green zone. The road is a futuristic data centre corridor with rows of GPU racks blurring in the background. Colours: race red, charcoal black, neon teal. The concept: blazing-fast, cost-efficient, self-hosted LLM inference — production-ready, no cloud dependency.

---

### Image 10 — NLP, Recommendation Systems & Time-Series Forecasting

Size 1280 × 720, Name= 10. NLP Recommendation Systems & Time-Series Forecasting.png

**Image about:**
A triptych-style wide illustration with three panels seamlessly blended together. Left panel: a text document with sentiment analysis visualised as a glowing colour-coded heatmap over the words (green for positive, red for negative). Centre panel: a recommendation engine depicted as a stylised retail shelf that dynamically rearranges products based on a customer profile hovering above it. Right panel: a time-series graph of business metrics with an AI prediction line extending into the future, confidence intervals shaded in soft blue. The overall palette is clean white with deep-blue accents. The image communicates: production-grade applied ML solving real business challenges across language, personalisation, and prediction.

---

### Image 11 — AI Voice Agents (LiveKit, Retell, Vapi)

Size 1280 × 720, Name= 11. AI Voice Agents (LiveKit, Retell, Vapi).png

**Image about:**
A sleek, close-up illustration of a voice interaction happening in real time. A translucent sphere — the AI voice agent — floats in a professional workspace, pulsing with animated sound waves as it listens and responds. A timeline at the bottom shows real-time speech-to-text transcription, intent detection, and response generation — all happening within milliseconds. The background is a softly blurred office environment. Colours: clean white, electric blue, silver. The mood is helpful, professional, and instant — conveying an AI that speaks, listens, understands context, and delivers answers at human-conversation speed for enterprise call centres and customer engagement.

---

### Image 12 — No-Code Automation: N8N & Make

Size 1280 × 720, Name= 12. No-Code Automation_ N8N & Make.png

**Image about:**
A vibrant, energetic illustration of a no-code automation canvas. Dozens of app icons (CRM, email, Slack, database, spreadsheet, AI model) are connected by animated workflow arrows in a looping diagram. In the centre, a single trigger event (a new customer form submission) cascades through the entire network — each node lights up in sequence as data flows automatically. The background is a bright, clean white workspace. The style is modern SaaS product marketing illustration — flat 2D with subtle drop shadows. The concept: entire business workflows automated without writing a single line of code — saving hours, eliminating errors, connecting every tool.

---

### Image 13 — TensorFlow & PyTorch

Size 1280 × 720, Name= 13. TensorFlow & PyTorch.png

**Image about:**
A powerful, dark-themed illustration of two titans of the ML world working in harmony. On the left, a TensorFlow-inspired computational graph — nodes and tensors flowing in structured layers. On the right, a PyTorch-inspired dynamic graph — flexible, fluid, pythonic. Both converge into a single trained model at the centre — a glowing neural architecture standing strong like a monument. The background shows GPU clusters and floating gradient descent equations. The colour palette: TensorFlow orange meets PyTorch red in a shared deep-charcoal environment lit from below. The image communicates: mastery of the world's leading deep learning frameworks — from research prototype to production model.

---

## Mobile Full Stack

---

### Image 14 — React Native & Cross-Platform Mobile Development

Size 1280 × 720, Name= 14. React Native & Cross-Platform Mobile Development.png

**Image about:**
A wide, clean product-showcase illustration showing a single codebase splitting into two perfectly identical mobile app interfaces — an iPhone on the left and an Android phone on the right. The code is visualised as a glowing JSX component tree in the centre, forking like a tree branch into both devices. Both screens display the same beautiful, pixel-perfect UI — a modern dashboard app with charts and cards. The background has subtle code patterns. Colours: React blue, white, dark charcoal. The image communicates: write once, run everywhere — cross-platform mobile development that doesn't sacrifice quality, performance, or user experience on either platform.

---

### Image 15 — Native Android & iOS Development (Java/Kotlin/Swift)

Size 1280 × 720, Name= 15. Native Android & iOS Development.png

**Image about:**
A bold, split-screen illustration. Left half: a native Android interface glowing in Google Material You design language, with a Kotlin code snippet artistically overlaid. Right half: a native iOS interface in Apple's refined Human Interface Guidelines style, with Swift syntax elegantly printed over it. Between them, a performance benchmark graph shows native apps outperforming all others in speed and fluency. Both phones are held by stylised hands in a professional environment. The style is high-end product photography meets technical illustration. The concept communicates: deeply native mobile experiences — handcrafted for each platform's strengths, delivering maximum performance, security, and platform integration.

---

### Image 16 — Capacitor (Ionic) Mobile Development

Size 1280 × 720, Name= 16. Native Capacitor (Ionic) Mobile Development.png

**Image about:**
An isometric 3D illustration of a web application smoothly transforming into a mobile app. A web browser window on the left morphs into a phone on the right, with the web content adapting perfectly to the native mobile container. Native device APIs — camera, GPS, push notifications, biometrics — are visualised as glowing plug connectors attaching to the web app's core. The transformation is fluid and elegant. Background: soft gradient from white to light blue. The image conveys: the best of both worlds — web development speed and reach, combined with native mobile capabilities, deployed to iOS and Android from a single codebase.

---

## Web Full Stack

---

### Image 17 — Ruby on Rails 7 & 8 (Hotwire Native)

Size 1280 × 720, Name= 17. Ruby on Rails 7 & 8 (Hotwire Native).png

**Image about:**
A sophisticated, retro-meets-modern illustration celebrating Ruby on Rails. A vintage steam locomotive (the classic "Rails" metaphor) redesigned as a sleek, futuristic bullet train speeds along rails made of glowing HTML and Ruby code. The windows of the train display real-time Hotwire Turbo Frame updates — pages refreshing without full reloads, visualised as lightning bolts replacing reload spinners. The background is a stylised city of web applications being delivered at speed. Colours: ruby red, warm gold, charcoal. The concept: a battle-tested, convention-driven framework made faster and more reactive than ever — shipping production-grade web applications with elegant code.

---

### Image 18 — MERN Stack (MongoDB, Express, React, Node.js)

Size 1280 × 720, Name= 18. MERN Stack (MongoDB, Express, React, Node.js).png

**Image about:**
A clean, layered architecture diagram rendered as a beautiful 3D building cross-section. The foundation (bottom layer) is a glowing MongoDB database — JSON documents stacked like bricks. The middle floor is an Express.js API layer, shown as a well-organised routing switchboard with green connection lines. The next floor up is a Node.js runtime — an engine room running JavaScript at server speed. At the top, a React frontend renders a pixel-perfect UI overlooking the city below. Each layer connects to the next via glowing elevator shafts of data. The style is isometric, modern, and colourful. The image conveys a unified, JavaScript-powered full-stack architecture — one language, every layer, end-to-end.

---

### Image 19 — MEAN Stack (MongoDB, Express, Angular, Node.js)

Size 1280 × 720, Name= 19. MEAN Stack (MongoDB, Express, Angular, Node.js).png

**Image about:**
A dynamic enterprise-scale web platform illustration. A large, glowing TypeScript-powered Angular front-end fills the top half of the image — complex dashboards, data tables, and reactive forms assembled with rigid engineering precision. Below it, a transparent layer reveals the Node.js and Express.js backend powering every API call, with MongoDB housing structured collections of business data. Data flows upward in clean API response ribbons. The background suggests a corporate enterprise environment: a tall glass office building. Colours: Angular red, MongoDB green, Node.js dark green, all on a navy background. The concept: enterprise-grade, TypeScript-first full-stack development for complex, scalable business applications.

---

## Web Frontend

---

### Image 20 — React + TypeScript

Size 1280 × 720, Name= 20. React + TypeScript.png

**Image about:**
A vibrant, modern developer-experience illustration. A large monitor displays a React component tree rendered in a split view: on the left, clean TypeScript code with coloured type annotations highlighted; on the right, the live rendered UI — a beautiful, pixel-perfect web application with smooth animations. Around the screen, floating badges show: type safety, zero runtime errors, reusable components, fast rendering. The background is a dark IDE theme (VS Code inspired). Colours: React blue, TypeScript blue, white. The mood is professional and productive — communicating that type-safe React development eliminates entire classes of bugs while enabling large-scale, maintainable frontend codebases.

---

### Image 21 — Next.js (SSR, SSG, Edge)

Size 1280 × 720, Name= 21. Next.js (SSR, SSG, Edge).png

**Image about:**
A cinematic, high-speed illustration of a web page being served from the edge — milliseconds before the user even clicks. A globe with glowing edge node locations (London, Mumbai, Singapore, New York, Sao Paulo) is shown with request paths routing to the nearest node. From each node, a fully server-rendered page flies into a browser like a paper airplane at the speed of light. A performance score of 100/100 glows in the corner. The background is dark space with warm city light reflected below the globe. Colours: Next.js black, white, gold. The concept: a full-stack React framework that delivers pages at the speed of light — SEO-ready, globally distributed, and production-perfect.

---

### Image 22 — HTML, CSS & Tailwind CSS

Size 1280 × 720, Name= 22. HTML, CSS & Tailwind CSS.png

**Image about:**
A delightful, colourful illustration of a web page being built in real time — like an artist painting on a canvas. Utility class labels (rounded-xl, bg-blue-500, flex, gap-4, text-lg) float out of a Tailwind CSS palette like brushstrokes and land precisely onto the UI components they style. The page design is beautiful — modern cards, clean typography, responsive grid. The artist is represented as a stylised cursor moving with creative precision. The background is a bright white design studio. The mood is creative, fast, and joyful — communicating that Tailwind CSS turns styling from a chore into a superpower, producing beautiful, consistent UIs at developer speed.

---

## Design

---

### Image 23 — UI/UX Design Process (Figma, Adobe XD)

Size 1280 × 720, Name= 23. UI-UX Design Process (Figma, Adobe XD).png

**Image about:**
A wide, warm illustration of the end-to-end product design journey laid out as a horizontal timeline. From left to right: a rough paper sketch, a digital wireframe in Figma, a colour-rich high-fidelity prototype, a user testing session with feedback annotations, and finally a pixel-perfect developer handoff screen showing redlines and component specs. Each stage is beautifully illustrated with warm pastels and soft shadows. Design tools are represented as subtle icon overlays at each stage. The style is editorial and warm — not cold and technical. The concept: thoughtful, user-centred design that bridges business goals and human needs — producing interfaces that are both beautiful and genuinely usable.

---

### Image 24 — Brand Identity & Visual Design (Illustrator, Photoshop, Sketch)

Size 1280 × 720, Name= 24. Brand Identity & Visual Design (Illustrator, Photoshop, Sketch).png

**Image about:**
A richly detailed illustration of a brand identity system being built in a design studio. At the centre is a logo mark evolving through iterations — rough sketches on the left transforming into a polished vector mark on the right. Surrounding it are brand assets arranged in a mood board: colour palettes, typography specimens, icon sets, business cards, packaging mockups, and a style guide document. The workspace is warm and creative — wooden desk, natural light, coffee cup. Colours: warm cream, terracotta, gold, deep navy. The image communicates: cohesive, strategic visual design that gives businesses a compelling, consistent identity across every touchpoint.

---

### Image 25 — Design Systems & Component Libraries

Size 1280 × 720, Name= 25. Design Systems & Component Libraries.png

**Image about:**
A precise, beautiful isometric 3D illustration of a design system as a structured component library. Rows of reusable UI components (buttons in all states, input fields, cards, navigation bars, modals, data tables) sit on glowing shelves in an organised digital library. Each component is labelled with its token values — spacing, colour, typography. A product screen is being assembled in the foreground — a developer picks components off the shelf and snaps them together like LEGO, building a complete interface in minutes. The style is clean, technical, and professional. The concept: scalable, consistent product design — one source of truth that speeds up both design and development.

---

## DevOps

---

### Image 26 — Docker & Containerisation

Size 1280 × 720, Name= 26. Docker & Containerisation.png

**Image about:**
A bold, striking illustration of software containerisation using the classic shipping container metaphor elevated to a beautiful technical artwork. A large cargo ship sails through a digital ocean — its containers are neatly stacked, each one labelled with a service name (API, database, cache, worker, frontend). The containers are translucent, showing the running application inside each one — isolated but interconnected. A crane (the Docker daemon) efficiently loads and unloads containers. The water is stylised as flowing data streams. Colours: Docker blue, ocean teal, steel grey, white. The concept: consistent, isolated, portable application packaging — ship any app to any environment without surprises.

---

### Image 27 — Kubernetes Orchestration

Size 1280 × 720, Name= 27. Kubernetes Orchestration.png

**Image about:**
A commanding, dramatic illustration of Kubernetes as a master conductor of a distributed computing symphony. The conductor (visualised as a Kubernetes cluster control plane) stands at a podium, arms raised, directing dozens of pod musicians — each playing their part in a perfectly coordinated performance. Nodes are sections of the orchestra (strings, brass, percussion). Auto-scaling is shown as new musicians seamlessly appearing when the music demands more volume. A self-healing moment is captured: one musician stumbles but the conductor instantly reassigns their part. Colours: Kubernetes blue, white, gold. The concept: intelligent, self-healing, auto-scaling container orchestration — keeping applications running perfectly at any scale.

---

### Image 28 — CI/CD Pipeline

Size 1280 × 720, Name= 28. CI-CD Pipeline.png

**Image about:**
A wide, energetic illustration of a CI/CD pipeline as a high-speed automated factory floor. Code commits enter as raw material on the left. They travel along a conveyor belt through successive automated stations: build compilation (sparks flying), unit test execution (green checkmarks lighting up), security scanning (a shield with a magnifying glass), staging deployment (a miniature replica environment), and finally production release (a green rocket launching). Each station is staffed by robotic arms — no humans required. Above the pipeline, a dashboard shows deployment frequency: multiple releases per day. Colours: electric green, charcoal, white. The concept: continuous, automated delivery — from code commit to production in minutes, every time.

---

### Image 29 — Cloud Monitoring & Observability

Size 1280 × 720, Name= 29. Cloud Monitoring & Observabilit.png

**Image about:**
A cinematic, dark-mode illustration of a world-class observability command centre. Three giant screens dominate the background: the left shows distributed tracing — a request's journey through 12 microservices visualised as a flame graph; the centre shows real-time metrics — CPU, memory, request rate, error rate — all trending healthy with a subtle AI anomaly detection alert appearing; the right shows aggregated logs with intelligent filtering. In the foreground, engineers are confidently reviewing dashboards — not frantically firefighting, but calmly understanding system behaviour. Colours: dark navy, teal, amber alerts, green healthy states. The concept: complete visibility into complex systems — understanding what's happening, why, and how to fix it before users notice.

---

### Image 30 — Full-Stack Cloud Architecture (AWS, GCP, Azure)

Size 1280 × 720, Name= 30. Full-Stack Cloud Architecture (AWS, GCP, Azure).png

**Image about:**
A grand, sweeping architectural diagram rendered as a photorealistic 3D landscape. A modern cloud infrastructure is visualised as a futuristic smart city — different cloud regions are neighbourhoods connected by glowing data highways. Key architectural components are distinct buildings: a load balancer skyscraper at the city entrance, a Kubernetes cluster neighbourhood of identical towers, a managed database district, a serverless functions quarter with ephemeral pop-up buildings, and a CDN ring of satellite towers at the city perimeter. The whole city hums with data traffic, visualised as glowing vehicle streams. The sky shows multi-cloud connections between cities. Colours: cloud blue (AWS orange accents), cloud white, metallic silver. The concept: robust, scalable, multi-cloud infrastructure architecture — designed for enterprise reliability, security, and global performance.

---

## 7. Summary Reference Table

| # | Image Title | Category | Key Technologies |
|---|-------------|----------|-----------------|
| 01 | Custom LLM Development | AI & ML | LLM, Neural Networks |
| 02 | Fine-Tuning LLMs & SLMs | AI & ML | Fine-tuning, Open-Weight Models |
| 03 | Reinforcement Learning | AI & ML | RLHF, DPO, GRPO, DQN |
| 04 | LLM Orchestration | AI & ML | Harness, Multi-model |
| 05 | AI Agents | AI & ML | OpenClaw, NanoClaw, Hermes |
| 06 | MLOps Pipeline | AI & ML | MLflow, W&B, Kubeflow, SageMaker |
| 07 | Vector Databases | AI & ML | Pinecone, FAISS, PGVector, Chroma |
| 08 | LangChain & LlamaIndex | AI & ML | LangChain, LangFlow, LlamaIndex |
| 09 | vLLM & Llama.cpp | AI & ML | Llama.cpp, vLLM, Inference |
| 10 | Applied ML (NLP/Rec/TS) | AI & ML | NLP, Recommendations, Forecasting |
| 11 | AI Voice Agents | AI & ML | LiveKit, Retell, Vapi |
| 12 | No-Code Automation | AI & ML | N8N, Make |
| 13 | TensorFlow & PyTorch | AI & ML | TensorFlow, PyTorch |
| 14 | React Native (Cross-Platform) | Mobile | React Native, Node.js, Rails |
| 15 | Native Android & iOS | Mobile | Kotlin, Swift, Java |
| 16 | Capacitor / Ionic | Mobile | Capacitor, Ionic, Hybrid |
| 17 | Ruby on Rails 7 & 8 | Web Full Stack | Rails, Hotwire |
| 18 | MERN Stack | Web Full Stack | MongoDB, Express, React, Node |
| 19 | MEAN Stack | Web Full Stack | MongoDB, Express, Angular, Node |
| 20 | React + TypeScript | Web Frontend | React, TypeScript |
| 21 | Next.js | Web Frontend | Next.js, SSR, SSG, Edge |
| 22 | HTML/CSS/Tailwind | Web Frontend | Tailwind CSS |
| 23 | UI/UX Design Process | Design | Figma, Adobe XD |
| 24 | Brand Identity & Visual | Design | Illustrator, Photoshop, Sketch |
| 25 | Design Systems | Design | Components, Tokens |
| 26 | Docker Containerisation | DevOps | Docker |
| 27 | Kubernetes Orchestration | DevOps | Kubernetes |
| 28 | CI/CD Pipeline | DevOps | CI/CD, GitHub Actions |
| 29 | Cloud Monitoring | DevOps | Observability, Monitoring |
| 30 | Cloud Architecture | DevOps | AWS, GCP, Azure |

---

## Reference workflow

1. Read the blog draft — identify primary topic and technology focus
2. Open Section 7 (Summary Reference Table) — filter by category and key technologies
3. Read **Image about** for top 1-2 candidates — confirm the thematic description matches the blog's tone and subject
4. Select 1 hero image (1280×720) — the image whose topic most directly matches the blog's primary subject
5. Verify the file exists at `drafts/images_to_use/images/pre_images/AI_Blog_1280_720/<filename>`
6. Record selection in `images/manifest.json` (see `image-prompts` skill for manifest format)
7. Hand off manifest to `wordpress-publishing` for upload
