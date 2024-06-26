# theme.py

custom_ui_css = """
/* Fade-in Animation for Headings and Paragraphs */
@keyframes fade-in {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

/* Slide-in Animation for Lists and Headings */
@keyframes slide-in {
    from {
        transform: translateY(-50px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

/* RGB Line Animation */
@keyframes rgb {
    0% {
        background-color: red;
    }
    33% {
        background-color: green;
    }
    67% {
        background-color: blue;
    }
    100% {
        background-color: red;
    }
}

/* Apply fade-in animation to headings and paragraphs */
h1, h2, p {
    animation: fade-in 2s ease-out;
    color: white; /* Text color */
}

/* Apply slide-in animation to lists */
ul {
    list-style-type: none;
    padding: 0;
    animation: slide-in 2s ease-out;
    color: white; /* Text color */
}

/* Styling for Links */
a {
    color: #ccc; /* Link color */
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* RGB Line Style */
.rgb-line {
    height: 10px; /* Adjust the height here */
    width: 100%;
    animation: rgb 5s infinite;
}

/* Body Style */
body {
    background-color: black; /* Background color */
    color: white; /* Default text color */
}
"""

custom_ui_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>FᴀsᴛAɴɪᴍᴇAᴘɪ Documentation</title>
    <style>
        {custom_ui_css}
    </style>
</head>
<body>
    <img src="https://telegra.ph/file/bde9c706821eacec414ed.jpg" alt="FastAnimeAPI Logo">
    <h1>Welcome to FᴀsᴛAɴɪᴍᴇAᴘɪ Documentation</h1>
    <p class="fade-in">Use the API endpoints listed below to interact with FᴀsᴛAɴɪᴍᴇAᴘɪ.</p>

    <div class="rgb-line"></div>

    <h2 class="slide-in">API Endpoints</h2>
    <ul class="slide-in">
        <li><a href="/docs/latest">Latest Anime Scrapper</a> - Get the latest released anime</li>
        <li><a href="/docs/search">Search Anime</a> - Search for anime</li>
        <li><a href="/docs/anime">Anime Information</a> - Get information about a specific anime</li>
        <li><a href="/docs/episode">Episode Information</a> - Get information about a specific episode</li>
        <li><a href="/docs/stream">Episode Stream</a> - Get stream links for an episode</li>
    </ul>

    <div class="rgb-line"></div>
</body>
</html>
"""
