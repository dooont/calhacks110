# components/MapComponent.py

import reflex as rx

class MapComponent(rx.Component):
    def render(self, **props):
        return rx.box(
            rx.el.div(
                id='map',
                style={
                    'width': '100%',
                    'height': '100vh',
                }
            ),
            rx.el.script(src='https://api.mapbox.com/mapbox-gl-js/v2.14.1/mapbox-gl.js'),
            rx.el.link(
                href='https://api.mapbox.com/mapbox-gl-js/v2.14.1/mapbox-gl.css',
                rel='stylesheet'
            ),
            rx.el.script(
                f"""
                mapboxgl.accessToken = 'pk.eyJ1IjoiZnJhbmtjaGFuZzEwMDAiLCJhIjoiY20xbGFzcG1hMDNvaTJxbjY3a3N4NWw4dyJ9.W78DlIwDnlVOrCE5F1OnkQ';
                const map = new mapboxgl.Map({{
                    container: 'map',
                    style: 'mapbox://styles/mapbox/streets-v11',
                    center: [-122.4194, 37.7749], // Centered on San Francisco
                    zoom: 12
                }});

                const toilets = {props.get('toilets')};

                toilets.forEach(function(toilet) {{
                    new mapboxgl.Marker()
                        .setLngLat([toilet.longitude, toilet.latitude])
                        .setPopup(new mapboxgl.Popup().setHTML(
                            `<h3>${{toilet.name}}</h3>
                            <p>Type: ${{toilet.resource_type}}</p>
                            <p>Access: ${{toilet.access}}</p>`
                        ))
                        .addTo(map);
                }});
                """
            ),
        )
