
from flask import Flask, render_template, request

app = Flask(__name__)

videos = [
    {
        "id": "ysz5S6PUM-U",
        "title": "Big Buck Bunny - Animated Movie",
        "channel": "Blender Studio",
        "category": "Movies",
        "views": "1.2M views"
    },
    {
        "id": "aqz-KE-bpKQ",
        "title": "Big Buck Bunny - Nature Video",
        "channel": "Nature Videos",
        "category": "Nature",
        "views": "850K views"
    },
    {
        "id": "ScMzIvxBSi4",
        "title": "Sample Video for Learning",
        "channel": "Learning Channel",
        "category": "Education",
        "views": "500K views"
    },
    {
        "id": "M7lc1UVf-VE",
        "title": "YouTube Player Demo",
        "channel": "YouTube Developers",
        "category": "Technology",
        "views": "2M views"
    }
]


@app.route("/")
def home():
    search = request.args.get("search", "").strip()
    category = request.args.get("category", "All")

    filtered_videos = videos

    if category != "All":
        filtered_videos = [
            v for v in filtered_videos
            if v["category"] == category
        ]

    if search:
        filtered_videos = [
            v for v in filtered_videos
            if search.lower() in v["title"].lower()
            or search.lower() in v["channel"].lower()
        ]

    return render_template(
        "index.html",
        videos=filtered_videos,
        search=search,
        category=category
    )


@app.route("/watch/<video_id>")
def watch(video_id):
    video = next(
        (v for v in videos if v["id"] == video_id),
        None
    )

    if video is None:
        return "Video not found", 404

    return render_template("index.html", videos=[video],
                           search="", category="All",
                           selected_video=video)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
