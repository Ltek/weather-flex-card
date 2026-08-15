# Weather Flex Card

The Most Flexible and Feature Rich Weather Card available for Home Assistant.

A fully-customizable weather card that lets you build exactly the weather display you want — current conditions, hourly/daily forecasts, a sky-brightness gradient bar, a sunrise/sunset arc, and a digital clock — each an independent, reorderable section with its own styling. Every section can pull from multiple weather entities and your own sensors.

... all in a super easy to use Visual Editor — no YAML required unless you prefer it.

https://github.com/Ltek/weather-flex-card

### ✨ Features

* **Sectioned, reorderable layout** – The card is built from independent sections — **Current Weather Header, Current Weather Metrics, Hourly Forecast, Daily Forecast, Sky Bar, Sun Position, and Clock & Date**. Drag to reorder, show/hide any section, and style each one on its own.
* **Multiple weather sources** – Set a **Primary** weather entity, a **Fallback** entity, and **per-metric Custom overrides** (any entity — a weather integration *or* your own sensor). Resolution runs Custom → Primary → Fallback → blank, so you can mix the best data source for each value. Forecasts merge across multiple entities.
* **Card Appearance** – Full card-wrapper styling to match any dashboard: border (per-side toggles + per-corner rounding), background color, glow, and a separate drop-shadow (color / X / Y / blur / spread / opacity). Custom weather-condition icon path and moon-phase shading included.
* **Current Weather Header** – Independent size controls for the condition icon, condition text, and temperature; a configurable sub-header metric (defaults to today's high/low), a custom friendly name, and a header metrics row drawn from built-in metrics and/or any entity.
* **Current Weather Metrics** – Display any set of weather metrics as a **Grid/Wrap list or as Chips**. Chips are fully styleable (text size, icon size, icon color, pill or custom corner radius, columns, show name/icon, hide-when-empty). Global value styling with per-value "Custom" overrides.
* **Hourly & Daily Forecasts** – Each type independently controls its **display mode** (Simple or Chart), **extra attribute**, **chart attribute**, and **number of slots** to show. Load only the forecast types you display to reduce websocket load on constrained devices.
* **Sky Bar** *(brightness & color gradient)* – A time-axis gradient showing day/night brightness and cloud cover. Configure the **timeframe** (fixed hours / full day / match the Sun Position arc), bar size and gradient colors, current-time marker, sunrise/sunset markers, and time labels + tick marks with adjustable **"show a label/tick every N hours"** spacing.
  * **Forecast Weather Metrics on the bar** – Overlay temps, condition icons, and extra attributes (wind, precipitation probability, UV, etc.) directly on the bar. Full ordering and per-side placement (above / on / below), with per-metric overrides for color, size, legibility, and **"Show every"** sampling — *every forecast hour, on tick marks, between tick marks, or every N hours*.
* **Sun Position arc** – A sunrise → solar-noon → sunset arc with a live sun marker, configurable window, tick marks, and sunrise/sunset time labels and icons.
* **Clock & Date** – An optional digital clock and date rendered in the header row. Independent placement, 12/24-hour format, seconds, popular date-format presets, per-element fonts/colors, and separate **text-legibility** (shadow/outline/auto) options for the time and the date.
* **Per-section styling** – Every section shares a consistent **Section Styles** panel: flush-to-edge/top/bottom, section dividers (above/below with thickness, length, style, color), and a semi-transparent section background — all with independent values per section.
* **Full visual editor** – Everything is configurable through the visual editor, organized into collapsible panels and sub-panels with per-section Reset buttons, modern sliders/dropdowns, and a read-only YAML view. Optional auto-collapse keeps the editor tidy.

### 🚀 Installation

1. Create the folder `\config\www\community\weather-flex-card`
2. Download [`weather-flex-card.js`](https://github.com/Ltek/weather-flex-card/blob/main/weather-flex-card.js) and place it in that folder.
3. Add as a Dashboard Resource:
   * Go to Settings > Dashboards > three-dot menu > Add Resource
   * Enter `/local/community/weather-flex-card/weather-flex-card.js` and select "JavaScript Module"
   * Click "Add"
4. Clear your browser cache and refresh.

### 📸 Screenshots

Example showing just a fraction of the available options...

<img width="400" alt="screen3" src="https://github.com/user-attachments/assets/595bb1a0-ea1b-4617-ab3e-681ef40bbe96" />
<img width="450" alt="screen2" src="https://github.com/user-attachments/assets/4b547210-b469-46f4-a661-b5f2894e1383" />
<img width="500" alt="screen1" src="https://github.com/user-attachments/assets/c8beb90a-7309-4383-b4b4-d02697503f01" />
<img width="500" alt="Copilot_20260815_161729" src="https://github.com/user-attachments/assets/391b0482-5a1c-40be-b353-f291e2332eb3" />
