# Digital Clock - Multiple Time Zones

A beautiful, responsive digital clock that displays the current time across 8 major time zones around the world.

## Features

✨ **Real-time Updates** - Clock updates every second
🌍 **8 Global Time Zones** - New York, London, Tokyo, Sydney, Dubai, São Paulo, Moscow, and Singapore
📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile devices
🎨 **Modern UI** - Sleek dark theme with glowing cyber effects
⚡ **Fast Performance** - Lightweight and optimized code
🔄 **Auto-refresh** - Updates when tab becomes visible

## Time Zones Supported

| City | Timezone | UTC Offset |
|------|----------|-----------|
| New York | EST/EDT | UTC-5/-4 |
| London | GMT/BST | UTC+0/+1 |
| Tokyo | JST | UTC+9 |
| Sydney | AEDT/AEST | UTC+10/+11 |
| Dubai | GST | UTC+4 |
| São Paulo | BRT/BRST | UTC-3/-2 |
| Moscow | MSK | UTC+3 |
| Singapore | SGT | UTC+8 |

## How to Use

1. Open `index.html` in your web browser
2. The clocks will automatically start displaying current times
3. Times update every second
4. View your local time at the bottom

## File Structure

```
clock/
├── index.html       # HTML template
├── styles.css       # Styling and animations
└── script.js        # Clock logic and updates
```

## Technical Details

- **HTML5** - Semantic markup
- **CSS3** - Advanced styling with animations and gradients
- **Vanilla JavaScript** - No dependencies required
- **Responsive Grid** - Auto-adapts to screen size

## Browser Support

- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera
- All modern mobile browsers

## Customization

### Add More Time Zones

Edit `script.js` and add to the `timeZones` object:

```javascript
const timeZones = {
    'clock-newyork': 'America/New_York',
    'clock-custom': 'Asia/Hong_Kong',  // Add your timezone
    // ... more zones
};
```

Then add corresponding HTML in `index.html`:

```html
<div class="clock-card">
    <h2>Hong Kong</h2>
    <p class="timezone">HKT (UTC+8)</p>
    <div class="digital-clock" id="clock-custom">00:00:00</div>
</div>
```

### Modify Colors

Edit the CSS variables in `styles.css`:
- Primary color: `#00d4ff` (cyan)
- Secondary color: `#00ff88` (lime green)
- Background: `linear-gradient(135deg, #1e1e2e 0%, #0f3460 100%)`

## License

MIT License - Feel free to use and modify!
