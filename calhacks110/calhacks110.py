"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def create_subtitle_heading(text):
    """Create a subtitle heading with specific styling."""
    return rx.heading(
        text,
        font_weight="500",
        margin_bottom="0.5rem",
        font_size="1.125rem",
        line_height="1.75rem",
        as_="h3",
        color="black",
    )


def create_section_heading(text):
    """Create a section heading with specific styling."""
    return rx.heading(
        text,
        font_weight="600",
        margin_bottom="1rem",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h2",
        color="black",
    )


def create_form_label(label_text):
    """Create a form label with specific styling."""
    return rx.el.label(
        label_text,
        display="block",
        font_weight="500",
        margin_bottom="0.25rem",
        color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_number_input(input_id, input_name):
    """Create a number input field with specific styling."""
    return rx.el.input(
        id=input_id,
        name=input_name,
        type="number",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#3B82F6",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        width="100%",
        background_color="#ffffff",
    )


def create_labeled_number_input(
    label_text, input_id, input_name
):
    """Create a labeled number input field."""
    return rx.box(
        create_form_label(label_text=label_text),
        create_number_input(
            input_id=input_id, input_name=input_name
        ),
    )


def create_select_option(option_value, option_text):
    """Create a select option with a value and text."""
    return rx.el.option(option_text, value=option_value)


def create_info_text(text):
    """Create an informational text with specific styling."""
    return rx.text(
        text,
        margin_bottom="0.5rem",
        color="#4B5563",
        font_size="0.875rem",
        line_height="1.25rem",
        background_color="white,"
    )


def create_learn_more_link():
    """Create a 'Learn More' link with specific styling."""
    return rx.el.a(
        "Learn More",
        href="#",
        _hover={"color": "#2563EB"},
        color="#3B82F6",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_scholarship_card(title, description, award_info):
    """Create a scholarship information card."""
    
    return rx.box(
        create_subtitle_heading(text=title),
        create_info_text(text=description),
        create_info_text(text=award_info),
        create_learn_more_link(),
        border_width="1px",
        border_color="#E5E7EB",
        padding="1rem",
        border_radius="0.375rem",
    )


def create_name_input():
    """Create a name input field with specific styling."""
    return rx.el.input(
        id="name",
        name="name",
        type="text",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#3B82F6",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.375rem",
        width="100%",
    )


def create_notes_textarea():
    """Create a notes textarea with specific styling."""
    return rx.el.textarea(
        id="notes",
        name="notes",
        rows="4",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#3B82F6",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.375rem",
        width="100%",
        background_color="#ffffff",
    )


def create_submit_button():
    """Create a submit button for finding scholarships."""
    return rx.el.button(
        " Find Scholarships ",
        type="submit",
        background_color="#3B82F6",
        _focus={
            "outline-style": "none",
            "box-shadow": "0 0 0 var(--ring-offset-width) var(--ring-offset-color), var(--ring-shadow)",
            "--ring-color": "#3B82F6",
            "--ring-offset-width": "2px",
        },
        _hover={"background-color": "#2563EB"},
        margin_top="1rem",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        width="100%",
    )


def create_personal_info_form():
    """Create a form for personal information and scholarship search notes."""
    return rx.box(
        create_section_heading(text="Personal Information"),
        rx.form(
            rx.box(
                create_form_label(
                    label_text="Scholarship Search Notes"
                ),
                create_notes_textarea(),
                margin_bottom="1rem",
            ),
            create_submit_button(),
        ),
        padding="1.5rem",
        border_radius="0.5rem", 
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_category_select():
    """Create a select dropdown for scholarship categories."""
    return rx.el.select(
        create_select_option(
            option_value=True, option_text="All Categories"
        ),
        create_select_option(
            option_value="merit", option_text="Merit-based"
        ),
        create_select_option(
            option_value="need", option_text="Need-based"
        ),
        create_select_option(
            option_value="stem", option_text="STEM"
        ),
        create_select_option(
            option_value="diversity",
            option_text="Diversity",
        ),
        id="category",
        name="category",
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#3B82F6",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        width="100%",
        background_color="#ffffff",
    )


def create_scholarship_filters():
    """Create filters for scholarship search including award range and category."""
    return rx.box(
        create_subtitle_heading(text="Filters"),
        rx.box(
            create_labeled_number_input(
                label_text="Minimum Award",
                input_id="award-min",
                input_name="award-min",
            ),
            create_labeled_number_input(
                label_text="Maximum Award",
                input_id="award-max",
                input_name="award-max",
            ),
            rx.box(
                create_form_label(label_text="Category"),
                create_category_select(),
            ),
            gap="1rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
        ),
        margin_bottom="1rem",
    )


def create_available_scholarships_section():
    """Create a section displaying available scholarships with filters."""
    return rx.box(
        create_section_heading(
            text="Available Scholarships"
        ),
        create_scholarship_filters(),
        rx.box(
            create_scholarship_card(
                title="Merit Scholarship",
                description="For students with a GPA of 3.5 or higher",
                award_info="Award: $5,000",
            ),
            create_scholarship_card(
                title="STEM Opportunity Grant",
                description="For students pursuing degrees in Science, Technology, Engineering, or Mathematics",
                award_info="Award: $7,500",
            ),
            create_scholarship_card(
                title="Diversity in Education Scholarship",
                description="For underrepresented students in higher education",
                award_info="Award: $3,000",
            ),
            id="scholarships",
            display="flex",
            flex_direction="column",
            gap="1rem",
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_scholarship_finder_layout():
    """Create the main layout for the Scholarship Finder application."""
    return rx.box(
        rx.heading(
            "Scholarship Finder",
            font_weight="700",
            margin_bottom="2rem",
            font_size="1.875rem",
            line_height="2.25rem",
            text_align="center",
            as_="h1",
            color="black",
        ),
        rx.box(
            create_personal_info_form(),
            create_available_scholarships_section(),
            display="flex",
            flex_direction="column",
            gap="2rem",
        ),
        width="100%",
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
        padding_top="2rem",
        padding_bottom="2rem",
    )


def create_scholarship_finder_app():
    """Create the complete Scholarship Finder page with styling and layout."""
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
        rx.box(
            create_scholarship_finder_layout(),
            background_color="#F3F4F6",
            min_height="100vh",
        ),
    )

def index() -> rx.Component:
    return rx.container(
        create_scholarship_finder_app(),
        background_color="white",
    )


app = rx.App()
app.add_page(index)
