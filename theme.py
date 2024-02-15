# theme.py

custom_ui_html = """
<!DOCTYPE html>
<html>
<head>
    <title>FᴀsᴛAɴɪᴍᴇAᴘɪ Documentation</title>
    <link rel="stylesheet" type="text/css" href="/custom_ui/custom_ui.css">
</head>
<body>
    <img src="https://via.placeholder.com/150" alt="FastAnimeAPI Logo">
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

custom_ui_css = """
/* Custom UI Theme for FastAPI Documentation */

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
}

/* Apply slide-in animation to lists */
ul {
    list-style-type: none;
    padding: 0;
    animation: slide-in 2s ease-out;
}

/* Styling for Links */
a {
    color: #007bff;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* RGB Line Style */
.rgb-line {
    height: 5px;
    width: 100%;
    animation: rgb 5s infinite;
}
"""

