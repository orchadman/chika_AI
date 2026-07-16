# Chika Core: System Architecture

The following diagram illustrates the data flow and component isolation within the Chika Core ecosystem. To protect intellectual property, the internal logic of the **Cognitive Core** and **Execution Sandbox** is redacted from the public repository, but their structural relationships are mapped below.

```mermaid
graph TD
    %% --- Define Styles ---
    classDef public fill:#0a1e14,stroke:#00ffaa,stroke-width:1px,color:#fff
    classDef private fill:#1e0a0a,stroke:#ff003c,stroke-width:1px,color:#fff
    classDef engine fill:#0a101e,stroke:#00f3ff,stroke-width:1px,color:#fff
    classDef external fill:#1a1a1a,stroke:#555,stroke-width:1px,color:#fff

    %% --- User Layer ---
    User((User)):::external

    %% --- Presentation & Audio (Public) ---
    subgraph Public_Interface [Public Interface Layer]
        UI[PyWebView / HTML5 Canvas UI]:::public
        WS[Flask-SocketIO Server]:::public
        EARS[ears.py: Groq Whisper STT]:::public
        MOUTH[mouth.py: Kokoro ONNX / SAPI5 TTS]:::public
    end

    %% --- Cognitive Core (Private IP) ---
    subgraph Cognitive_Core [Cognitive Core - REDACTED IP]
        MAIN{main.py: Swarm Orchestrator}:::private
        ROUTER[Vector Semantic Router Matrix]:::private
        PULSE[The Pulse: Async Environmental Monitor]:::private
        MEM[memory_core.py: Background RAG Extractor]:::private
    end

    %% --- Inference Engine ---
    subgraph Inference_Engine [Local Inference Engine]
        OLLAMA[Ollama API]:::engine
        LLM[Llama 3.1 8b: Reasoning]:::engine
        QWEN[Qwen 2.5: Coder]:::engine
        MOON[Moondream: Vision Parser]:::engine
        
        OLLAMA --- LLM
        OLLAMA --- QWEN
        OLLAMA --- MOON
    end

    %% --- Execution Sandbox (Private IP) ---
    subgraph Execution_Sandbox [Execution Sandbox - REDACTED IP]
        TOOLS[tools.py: Dynamic Tool Registry]:::private
        DOCKER[Docker SDK: Isolated Workspace]:::private
        RPA[OpenCV + PyTesseract: OS Automation]:::private
        INJECT[Metacognitive Hot-Reload]:::private
    end

    %% --- Routing & Data Flow ---
    User -->|Voice| EARS
    User <-->|WebSocket Directives| UI
    UI <-->|JSON Payloads| WS
    MOUTH -->|Audio Synthesis| User

    WS <-->|Commands/Auth| MAIN
    EARS -->|Transcriptions| MAIN
    MAIN -->|Text Stream| MOUTH

    MAIN --- ROUTER
    MAIN --- PULSE
    MAIN --- MEM

    ROUTER -->|Agent Injection| OLLAMA
    PULSE -->|Spatial Screen States| MOON
    MEM -.->|Contextual Embedding| MAIN

    MAIN -->|Function Calling| TOOLS
    TOOLS -->|Builds/Serves| DOCKER
    TOOLS -->|Clicks/Types| RPA
    TOOLS -->|Writes New Synapses| INJECT
    INJECT -.->|Reboots| MAIN
