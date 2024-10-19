"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def create_header():
    """Create a header component with styled text and responsive container."""
    return rx.box(
        rx.heading(
            "Example Text",
            font_weight="700",
            font_size="1.5rem",
            line_height="2rem",
            color="#1F2937",
            as_="h1",
        ),        
        # style=rx.breakpoints(
        #     {
        #         "640px": {"max-width": "640px"},
        #         "768px": {"max-width": "768px"},
        #         "1024px": {"max-width": "1024px"},
        #         "1280px": {"max-width": "1280px"},
        #         "1536px": {"max-width": "1536px"},
        #     }
        # ),
        margin_left="auto",
        margin_right="auto",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="1.5rem",
        padding_bottom="1.5rem",
        width="100%",
    )


def create_get_started_button():
    """Create a 'Get Started' button component with styled attributes and responsive width."""
    return rx.el.a(
        " Get Started ",
        href="/dashboard",
        background_color="#2563EB",
        font_weight="700",
        _hover={"background-color": "#1D4ED8"},
        display="inline-block",
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        font_size="1.125rem",
        line_height="1.75rem",
        color="#ffffff",
        width=rx.breakpoints(
            {"0px": "100%", "640px": "auto"}
        ),
    )


def create_learn_more_button():
    """Create a 'Learn More' button component with styled attributes and responsive width."""
    return rx.el.a(
        " Learn More ",
        href="/signup",
        background_color="transparent",
        border_width="1px",
        border_color="#D1D5DB",
        font_weight="600",
        _hover={"background-color": "#E5E7EB"},
        display="inline-block",
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        color="#374151",
        font_size="1.125rem",
        line_height="1.75rem",
        width=rx.breakpoints(
            {"0px": "100%", "640px": "auto"}
        ),
    )


def create_hero_section():
    """Create the hero section with heading, description, and action buttons."""
    return rx.box(
        rx.heading(
            "Welcome to Our Service",
            font_weight="700",
            margin_bottom="2rem",
            font_size="3rem",
            line_height="1",
            color="#111827",
            as_="h2",
        ),
        rx.text(
            "Discover the best features and boost your productivity with our innovative solutions",
            margin_bottom="3rem",
            color="#4B5563",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        rx.box(
            create_get_started_button(),
            create_learn_more_button(),
            display="flex",
            flex_direction="column",
            gap="1.5rem",
        ),
        max_width="42rem",
        margin_left="auto",
        margin_right="auto",
        text_align="center",
    )


def create_footer():
    """Create a footer component with copyright information and styling."""
    return rx.box(
        rx.box(
            rx.text(
                "© 2023 Example Company. All rights reserved."
            ),
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1rem",
            padding_right="1rem",
            text_align="center",
        ),
        background_color="#1F2937",
        margin_top="5rem",
        padding_top="2rem",
        padding_bottom="2rem",
        color="#ffffff",
        width="100%",
    )


def create_main_content():
    """Assemble the main content of the landing page, including header, hero section, and footer."""
    return rx.box(
        rx.box(
            create_header(),
            background_color="#ffffff",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        rx.box(
            create_hero_section(),
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            # margin_left="auto",
            # margin_right="auto",
            padding_left="1rem",
            padding_right="1rem",
            padding_top="5rem",
            padding_bottom="5rem",
        ),
        create_footer(),
        background_color="#F3F4F6",
        font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
    )


def render_landing_page():
    """Render the complete landing page with styles, layout, and content components."""
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
    @font-face {
        font-family: 'LucideIcons';
        src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
    }
    """
        ),
        create_main_content(),
        padding="0px",
    )

def index() -> rx.Component:
    return rx.container(
        render_landing_page(),
        size="4",
        width="100%",
        height="100%",
    )


app = rx.App()
app.add_page(index)
