# 🧠 Chika Core: Autonomous Local Multi-Agent OS Copilot

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Automated_Sandboxing-2496ED.svg)
![WebSockets](https://img.shields.io/badge/WebSockets-Flask%20%7C%20SocketIO-black.svg)
![Local LLMs](https://img.shields.io/badge/LLMs-Ollama%20%7C%20Llama3.1-FF9D00.svg)
![Status](https://img.shields.io/badge/Status-Active_Development_(Closed_Core)-success.svg)

> **Developer Note:** *Chika Core is currently in active development for future commercial release. To protect proprietary logic—including the vector-based semantic routing matrix, The Pulse loop, and the metacognitive runtime—the core engine source code is kept in a private repository. This showcase repository contains architectural documentation, UI implementation samples, and system capability overviews.*

## 📌 Project Overview
Chika Core is an advanced, end-to-end local desktop artificial general intelligence (AGI) assistant. It features autonomous environment sensing, a dual-engine voice interface, a sandboxed DevOps development runner, and a custom semantic routing matrix. 

Unlike cloud-dependent AI wrappers, Chika Core is engineered strictly for **low-latency, localized execution**, ensuring absolute data privacy while maintaining complex multi-agent reasoning and physical OS automation.

## 🏗️ Core Architectural Highlights

### 1. Bi-Directional WebSocket UI Engine
Constructed a cyberpunk-themed interface powered by Flask and `SocketIO`, running inside a borderless, full-screen hardware-accelerated wrapper (`pywebview`)[cite: 1, 4]. The UI features:
*   A hardware-accelerated canvas audio visualizer that syncs with system state[cite: 1].
*   A dynamic command palette (triggered via `Ctrl+K`) for rapid agent routing and theme control[cite: 1].
*   A real-time authorization intercept modal to block high-threat autonomous terminal commands (e.g., `rm -rf`)[cite: 1, 4].

### 2. "The Pulse" (Asynchronous Perceptual Autonomy)
Engineered a persistent background thread (`the_pulse_loop`) that grants the system perceptual autonomy[cite: 4].
*   Silently monitors battery levels, system resources, and active screen states using localized vision models (`moondream`)[cite: 4].
*   Evaluates environmental data sequentially and autonomously decides whether to interrupt the user with verbal warnings or guidance, independent of user prompts[cite: 4].

### 3. Advanced CV / RPA Automation Pipeline
Replaced brittle coordinate-clicking with an advanced computer vision automation pipeline (`pyautogui` + `opencv` + `pytesseract` OCR)[cite: 6]. 
*   The agent parses spatial screen states, searches for specific visual UI element strings, calculates their exact X/Y center coordinates, and autonomously clicks them[cite: 6]. 
*   Capable of navigating complex user interfaces, such as autonomously locating and triggering "Next Episode" buttons on streaming platforms[cite: 6].

### 4. Semantic Router Matrix & Swarm Orchestration
Bypasses traditional keyword matching by utilizing dynamic vector embeddings (`nomic-embed-text`)[cite: 4, 10]. 
*   Uses mathematical cosine similarity to instantly map complex user directives to **8 core expert LLM profiles**[cite: 4].
*   Dynamically spawns specialist sub-agents from a registry of 70+ expert personas (e.g., Cyber Security Auditor, Windows Admin, Web Scraper) to handle complex, multi-step `swarm_orchestrate` tasks[cite: 2, 6].

### 5. Sandboxed Docker Development Pipeline
Features an automated, local DevOps sandbox utilizing the Docker SDK[cite: 6]. When prompted to generate web or game logic via localized code models (`qwen2.5-coder:7b`), Chika Core dynamically mounts workspace paths to isolated containers, exposes target ports, and serves applications instantly to `localhost`[cite: 6].

### 6. Continuous RAG & Dual-Engine Speech
*   **Memory Core:** A background thread silently harvests conversation logs, utilizes a structured LLM pipeline to isolate vital parameters, and indexes them into an absolute long-term vector file system without blocking the main event loop[cite: 4, 10].
*   **Speech Pipeline:** Features an ultra-fast, multi-threaded audio pipeline combining edge models and cloud fallbacks. Uses a queue-managed synthesis worker running a local Kokoro ONNX neural voice model (`bf_emma`) with a thread-safe Windows SAPI5 fallback[cite: 5]. Input is handled via noise-adjusted acoustic thresholds backed by `whisper-large-v3` (via Groq)[cite: 3].

## 💻 Hardware Optimization & Benchmarks
A major engineering focus for Chika Core was resource efficiency. The entire full-stack architecture—including heavy local LLM reasoning, ONNX inference, computer vision OCR, and Docker orchestration—is heavily optimized to run concurrently on standard consumer hardware. 

**Tested & Optimized Baseline Configuration:**
*   **System:** ASUS TUF Gaming F15
*   **GPU:** NVIDIA RTX 4060 (8GB VRAM)
*   **RAM:** 16GB
*   *Performance Note: Achieves low-latency asynchronous processing and sub-second UI rendering without requiring enterprise-grade VRAM clusters or continuous cloud computing costs.*

---
*Architected and developed by Aman Dubey. For professional inquiries regarding the architecture or implementation details, please reach out via LinkedIn or Email.*
