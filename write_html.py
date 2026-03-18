html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fazil AI</title>
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        :root {
            --bg-primary: #212121;
            --bg-secondary: #171717;
            --bg-hover: #2a2a2a;
            --bg-input: #2f2f2f;
            --text-primary: #ececec;
            --text-muted: #8e8ea0;
            --text-dim: #555;
            --accent: #19c37d;
            --accent-hover: #15a86a;
            --border: #3a3a3a;
            --user-bubble: #2a2a2a;
            --sidebar-width: 260px;
        }
        body { font-family: "Sora", sans-serif; background: var(--bg-primary); color: var(--text-primary); height: 100vh; display: flex; overflow: hidden; }
        .sidebar { width: var(--sidebar-width); background: var(--bg-secondary); display: flex; flex-direction: column; padding: 12px; flex-shrink: 0; border-right: 1px solid var(--border); }
        .sidebar-header { display: flex; align-items: center; justify-content: space-between; padding: 8px 6px 16px; }
        .logo { font-size: 15px; font-weight: 600; color: var(--text-primary); letter-spacing: -0.3px; }
        .logo span { color: var(--accent); }
        .new-chat-btn { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 10px; background: var(--accent); border: none; color: #fff; font-size: 13px; font-weight: 500; font-family: "Sora", sans-serif; cursor: pointer; width: 100%; transition: background 0.2s; margin-bottom: 20px; }
        .new-chat-btn:hover { background: var(--accent-hover); }
        .section-label { font-size: 10px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.8px; padding: 0 8px 8px; }
        .chat-history { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 2px; }
        .chat-history::-webkit-scrollbar { width: 3px; }
        .chat-history::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
        .chat-item { padding: 9px 12px; border-radius: 8px; font-size: 12.5px; color: var(--text-muted); cursor: pointer; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; transition: background 0.15s, color 0.15s; }
        .chat-item:hover { background: var(--bg-hover); color: var(--text-primary); }
        .chat-item.active { background: var(--bg-hover); color: var(--text-primary); }
        .sidebar-footer { margin-top: auto; border-top: 1px solid var(--border); padding-top: 12px; }
        .user-card { display: flex; align-items: center; gap: 10px; padding: 8px 10px; border-radius: 10px; cursor: pointer; transition: background 0.15s; }
        .user-card:hover { background: var(--bg-hover); }
        .avatar { width: 32px; height: 32px; border-radius: 50%; background: linear-gradient(135deg, #19c37d, #0ea5e9); display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; color: #fff; flex-shrink: 0; }
        .user-info { display: flex; flex-direction: column; }
        .user-name { font-size: 13px; font-weight: 500; color: var(--text-primary); }
        .user-plan { font-size: 10px; color: var(--text-dim); }
        .main { flex: 1; display: flex; flex-direction: column; min-width: 0; background: var(--bg-primary); }
        .topbar { display: flex; align-items: center; justify-content: space-between; padding: 14px 20px; border-bottom: 1px solid var(--border); flex-shrink: 0; }
        .model-badge { display: flex; align-items: center; gap: 6px; background: var(--bg-hover); border: 1px solid var(--border); border-radius: 8px; padding: 6px 12px; font-size: 12.5px; color: var(--text-primary); font-family: "Sora", sans-serif; cursor: pointer; }
        .model-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--accent); }
        .messages { flex: 1; overflow-y: auto; padding: 24px 0 16px; display: flex; flex-direction: column; }
        .messages::-webkit-scrollbar { width: 4px; }
        .messages::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
        .welcome { display: flex; flex-direction: column; align-items: center; justify-content: center; flex: 1; gap: 12px; padding: 40px 20px; text-align: center; animation: fadeIn 0.5s ease; }
        .welcome-icon { width: 52px; height: 52px; border-radius: 16px; background: linear-gradient(135deg, #19c37d22, #0ea5e922); border: 1px solid #19c37d44; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 4px; }
        .welcome h2 { font-size: 22px; font-weight: 600; color: var(--text-primary); letter-spacing: -0.5px; }
        .welcome p { font-size: 13px; color: var(--text-muted); max-width: 360px; line-height: 1.6; }
        .suggestion-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 12px; width: 100%; max-width: 480px; }
        .suggestion-card { background: var(--bg-hover); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; font-size: 12px; color: var(--text-muted); cursor: pointer; text-align: left; font-family: "Sora", sans-serif; transition: all 0.2s; line-height: 1.5; }
        .suggestion-card:hover { background: #333; color: var(--text-primary); border-color: #555; }
        .msg-row { display: flex; padding: 10px 20px; gap: 14px; animation: fadeIn 0.3s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
        .msg-row.user { flex-direction: row-reverse; }
        .msg-avatar { width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; flex-shrink: 0; margin-top: 2px; }
        .msg-avatar.ai { background: linear-gradient(135deg, #19c37d, #0ea5e9); color: #fff; }
        .msg-avatar.user-av { background: linear-gradient(135deg, #7c3aed, #5c5ce0); color: #fff; }
        .msg-content { max-width: 680px; display: flex; flex-direction: column; gap: 4px; }
        .msg-row.user .msg-content { align-items: flex-end; }
        .msg-name { font-size: 11px; color: var(--text-dim); font-weight: 500; }
        .msg-bubble { font-size: 14px; line-height: 1.75; color: var(--text-primary); }
        .msg-row.user .msg-bubble { background: var(--user-bubble); padding: 10px 16px; border-radius: 18px 18px 4px 18px; border: 1px solid var(--border); }
        .typing-indicator { display: flex; gap: 5px; align-items: center; padding: 6px 0; }
        .typing-indicator span { width: 7px; height: 7px; border-radius: 50%; background: var(--accent); animation: bounce 1.2s infinite; opacity: 0.7; }
        .typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
        .typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes bounce { 0%, 80%, 100% { transform: translateY(0); opacity: 0.4; } 40% { transform: translateY(-5px); opacity: 1; } }
        .input-area { padding: 12px 20px 20px; flex-shrink: 0; }
        .input-wrap { background: var(--bg-input); border: 1px solid var(--border); border-radius: 14px; overflow: hidden; transition: border-color 0.2s; max-width: 760px; margin: 0 auto; }
        .input-wrap:focus-within { border-color: #555; }
        textarea { width: 100%; background: transparent; border: none; outline: none; color: var(--text-primary); font-size: 14px; font-family: "Sora", sans-serif; padding: 14px 16px 8px; resize: none; min-height: 52px; max-height: 200px; line-height: 1.6; }
        textarea::placeholder { color: var(--text-muted); }
        .input-footer { display: flex; align-items: center; justify-content: flex-end; padding: 6px 12px 10px; gap: 8px; }
        .char-count { font-size: 11px; color: var(--text-dim); margin-right: auto; }
        .send-btn { width: 34px; height: 34px; border-radius: 9px; background: var(--accent); border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.2s; flex-shrink: 0; }
        .send-btn:hover { background: var(--accent-hover); transform: scale(1.05); }
        .send-btn:disabled { background: #333; cursor: not-allowed; transform: none; }
        .send-btn svg { width: 15px; height: 15px; fill: #fff; }
        .disclaimer { text-align: center; font-size: 11px; color: var(--text-dim); margin-top: 10px; max-width: 760px; margin-left: auto; margin-right: auto; }
        @media (max-width: 640px) { .sidebar { display: none; } .msg-content { max-width: 90vw; } }
    </style>
</head>
<body>
<div class="sidebar">
    <div class="sidebar-header">
        <div class="logo">Fazil <span>AI</span></div>
    </div>
    <button class="new-chat-btn" onclick="newChat()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12h14"/></svg>
        New chat
    </button>
    <div class="section-label">Recent</div>
    <div class="chat-history" id="chat-history">
        <div class="chat-item active">New conversation</div>
    </div>
    <div class="sidebar-footer">
        <div class="user-card">
            <div class="avatar">F</div>
            <div class="user-info">
                <span class="user-name">Fazil</span>
                <span class="user-plan">Fazil AI - Free</span>
            </div>
        </div>
    </div>
</div>
<div class="main">
    <div class="topbar">
        <div class="model-badge">
            <div class="model-dot"></div>
            Fazil AI - Llama 3.3
        </div>
    </div>
    <div class="messages" id="messages">
        <div class="welcome" id="welcome">
            <div class="welcome-icon">&#10022;</div>
            <h2>How can I help you?</h2>
            <p>I am Fazil AI, your personal assistant. Ask me anything - I am here to help.</p>
            <div class="suggestion-grid">
                <button class="suggestion-card" onclick="suggest(this)">Explain quantum computing simply</button>
                <button class="suggestion-card" onclick="suggest(this)">Write a Python function for me</button>
                <button class="suggestion-card" onclick="suggest(this)">Give me productivity tips</button>
                <button class="suggestion-card" onclick="suggest(this)">Help me draft an email</button>
            </div>
        </div>
    </div>
    <div class="input-area">
        <div class="input-wrap">
            <textarea id="user-input" placeholder="Message Fazil AI..." rows="1"></textarea>
            <div class="input-footer">
                <span class="char-count" id="char-count"></span>
                <button class="send-btn" id="send-btn" onclick="sendMessage()">
                    <svg viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
                </button>
            </div>
        </div>
        <div class="disclaimer">Fazil AI can make mistakes. Verify important information.</div>
    </div>
</div>
<script>
    const textarea = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const messagesDiv = document.getElementById("messages");
    const welcome = document.getElementById("welcome");
    const charCount = document.getElementById("char-count");
    let isTyping = false;
    textarea.addEventListener("input", function() {
        this.style.height = "auto";
        this.style.height = Math.min(this.scrollHeight, 200) + "px";
        charCount.textContent = this.value.length > 0 ? this.value.length + " chars" : "";
    });
    textarea.addEventListener("keydown", function(e) {
        if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sendMessage(); }
    });
    function suggest(btn) { textarea.value = btn.textContent; textarea.dispatchEvent(new Event("input")); sendMessage(); }
    function newChat() { messagesDiv.innerHTML = ""; messagesDiv.appendChild(welcome); welcome.style.display = "flex"; addHistoryItem("New conversation"); }
    function addHistoryItem(text) {
        const history = document.getElementById("chat-history");
        document.querySelectorAll(".chat-item").forEach(i => i.classList.remove("active"));
        const item = document.createElement("div");
        item.className = "chat-item active";
        item.textContent = text.length > 28 ? text.substring(0, 28) + "..." : text;
        history.insertBefore(item, history.firstChild);
    }
    async function sendMessage() {
        if (isTyping) return;
        const message = textarea.value.trim();
        if (!message) return;
        if (welcome.parentNode === messagesDiv) { welcome.style.display = "none"; addHistoryItem(message); }
        appendMessage("user", message);
        textarea.value = "";
        textarea.style.height = "auto";
        charCount.textContent = "";
        sendBtn.disabled = true;
        isTyping = true;
        const typingRow = appendTyping();
        try {
            const response = await fetch("/chat", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ message }) });
            const data = await response.json();
            typingRow.remove();
            appendMessage("ai", data.reply);
        } catch(err) {
            typingRow.remove();
            appendMessage("ai", "Sorry, something went wrong. Please try again.");
        }
        sendBtn.disabled = false;
        isTyping = false;
    }
    function appendMessage(type, text) {
        const row = document.createElement("div");
        row.className = "msg-row " + (type === "user" ? "user" : "");
        const av = document.createElement("div");
        av.className = "msg-avatar " + (type === "user" ? "user-av" : "ai");
        av.textContent = type === "user" ? "F" : "AI";
        const content = document.createElement("div");
        content.className = "msg-content";
        const name = document.createElement("div");
        name.className = "msg-name";
        name.textContent = type === "user" ? "You" : "Fazil AI";
        const bubble = document.createElement("div");
        bubble.className = "msg-bubble";
        bubble.textContent = text;
        content.appendChild(name);
        content.appendChild(bubble);
        row.appendChild(av);
        row.appendChild(content);
        messagesDiv.appendChild(row);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        return row;
    }
    function appendTyping() {
        const row = document.createElement("div");
        row.className = "msg-row";
        const av = document.createElement("div");
        av.className = "msg-avatar ai";
        av.textContent = "AI";
        const content = document.createElement("div");
        content.className = "msg-content";
        const name = document.createElement("div");
        name.className = "msg-name";
        name.textContent = "Fazil AI";
        const indicator = document.createElement("div");
        indicator.className = "typing-indicator";
        indicator.innerHTML = "<span></span><span></span><span></span>";
        content.appendChild(name);
        content.appendChild(indicator);
        row.appendChild(av);
        row.appendChild(content);
        messagesDiv.appendChild(row);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        return row;
    }
</script>
</body>
</html>'''

with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done! File written successfully!")
