import reflex as rx
config = rx.Config(
    app_name="campus_navigator",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)