# LNbits Table Town 🏘️

**Interactive Database Explorer for LNbits**

## 🎯 Overview

LNbits Table Town is an interactive database schema visualization that provides a comprehensive, zoomable, and filterable view of the LNbits database structure, including all extensions. It's designed for both developers and end-users to understand the LNbits ecosystem.

**Live Demo**: [https://arbadacarbayk.github.io/LNbits_TableTown/](https://arbadacarbayk.github.io/LNbits_TableTown/)

**Author**: [arbadacarbayk](https://github.com/arbadacarbaYK) | [info@plebtag.com](mailto:info@plebtag.com)

## 🚀 Features

### 🎮 Interactive Interface
- **Zoomable & Pannable**: Navigate large schemas with mouse/touch gestures
- **Real-time Search**: Find tables and extensions instantly
- **Smart Filtering**: Filter by category (Onchain, Nostr, Gaming, etc.)
- **Dual Views**: Switch between Developer and End-user perspectives
- **Responsive Design**: Works on desktop, tablet, and mobile

### 🎨 Visual Design
- **Color-coded Categories**: Each extension type has its own color
- **Core Tables**: Always visible in the center
- **Dependency Lines**: Visual connections between related tables
- **Interactive Tooltips**: Detailed information on hover
- **Highlight System**: Click to highlight dependencies

### 📊 Comprehensive Data
- **50+ Extensions**: Complete database models for all vetted extensions
- **Table Definitions**: Fields, relationships, and descriptions
- **Dependency Mapping**: Shows which extensions depend on core tables
- **GitHub Links**: Direct links to extension repositories

## 🎯 Categories

### 🔵 Core LNbits
- **Account**: User accounts and authentication
- **Wallet**: Lightning wallets for users
- **Payment**: Payment transaction records
- **AccessControlList**: API access control
- **UserAcls**: User access control lists

### 🟠 Onchain Features
- **SatsPay**: Accept Bitcoin payments on websites
- **Boltz**: Swap between onchain and Lightning
- **WatchOnly**: Monitor onchain Bitcoin addresses
- **SellCoins**: Sell coins for fiat

### 🟣 Nostr Integration
- **NostrMarket**: Sell products on Nostr marketplace
- **NostrRelay**: Launch your own Nostr relay
- **NostrClient**: Nostr client for extensions
- **NostrNip5**: Verify addresses for Nostr NIP-5

### 🟡 Gaming & Entertainment
- **SatsDice**: Play provably fair dice games
- **Coinflip**: Bet sats on coinflips
- **Numbers**: Block-based numbers game
- **Eightball**: Magic 8ball with payments

### 🔴 E-commerce & Business
- **Events**: Sell event tickets and manage attendees
- **Invoices**: Create invoices for clients
- **Paywall**: Create paywalls for content
- **AuctionHouse**: Digital goods auctions

### ⚫ Hardware & IoT
- **BitcoinSwitch**: Control devices with Bitcoin payments
- **LNURLDevice**: Control IoT devices with LNURL
- **Bleskomat**: ATM integration
- **FOSSA**: DIY Bitcoin ATM

### 🟤 Communication & Social
- **TipJar**: Accept Bitcoin donations with messages
- **StreamAlerts**: Bitcoin donations in stream alerts
- **Copilot**: Video tips/animations for streamers
- **SMTP**: Email service for sats

## 🎮 How to Use

### 1. **Open the Interface**
```bash
# Open in your web browser
open lnbits_schema_interactive.html
```

### 2. **Navigate the Schema**
- **Zoom**: Use mouse wheel or zoom controls
- **Pan**: Click and drag to move around
- **Reset**: Click the home button to reset view

### 3. **Filter Extensions**
- **All Extensions**: Show everything
- **Onchain**: Show only onchain-related extensions
- **Nostr**: Show only Nostr integration extensions
- **Gaming**: Show only gaming extensions
- **E-commerce**: Show only business extensions
- **Hardware**: Show only hardware/IoT extensions
- **Social**: Show only communication extensions

### 4. **Search Functionality**
- Type in the search box to find specific tables or extensions
- Search works across table names and extension names
- Results update in real-time

### 5. **Explore Dependencies**
- **Click on Core Tables**: See which extensions depend on them
- **Click on Extension Tables**: See their relationships to core
- **Click on Extensions**: Highlight the entire extension group
- **Click on Empty Space**: Reset all highlights

### 6. **Switch Views**
- **Developer View**: Shows technical details, field definitions, GitHub links
- **End-User View**: Shows user-friendly descriptions and use cases

## 🛠️ Technical Details

### File Structure
```
lnbits_schema_interactive.html    # Main interactive interface
lnbits_extensions_data.json       # Comprehensive extension data
LNBITS_INTERACTIVE_SCHEMA_DESIGN.md  # Design documentation
LNBITS_INTERACTIVE_SCHEMA_README.md  # This file
```

### Data Structure
The `lnbits_extensions_data.json` file contains:
- **Core Tables**: Complete definitions with fields and relationships
- **Extensions**: All 50+ vetted extensions with their database models
- **Categories**: Color coding and descriptions for each category
- **Dependencies**: Which extensions depend on core tables

### Technologies Used
- **D3.js**: Interactive visualizations and zoom/pan functionality
- **SVG**: Scalable vector graphics for crisp rendering
- **CSS Grid**: Responsive layout management
- **JavaScript**: Interactive filtering and search

## 🎯 Use Cases

### For Developers
- **Database Design**: Understand LNbits database structure
- **Extension Development**: See how extensions integrate with core
- **API Integration**: Understand table relationships and foreign keys
- **Dependency Analysis**: See which extensions depend on core tables

### For End Users
- **Feature Discovery**: Learn what LNbits can do
- **Extension Selection**: Choose the right extensions for your needs
- **Understanding**: Get a visual understanding of the LNbits ecosystem
- **Planning**: Plan your LNbits setup based on available features

### For System Administrators
- **Database Planning**: Understand database requirements
- **Extension Management**: See which extensions to install
- **Performance**: Understand table relationships for optimization
- **Security**: Understand access control and permissions

## 🔧 Customization

### Adding New Extensions
1. Edit `lnbits_extensions_data.json`
2. Add new extension under `extensions` section
3. Define tables, dependencies, and metadata
4. Refresh the interface

### Modifying Categories
1. Edit the `categories` section in the JSON file
2. Update colors and descriptions
3. Refresh the interface

### Styling Changes
1. Edit the CSS section in the HTML file
2. Modify colors, fonts, and layout
3. Refresh the interface

## 🚀 Future Enhancements

### Planned Features
- **Export Functionality**: Export filtered views as images
- **Print Support**: Generate printable documentation
- **API Integration**: Real-time data from LNbits instances
- **3D Visualization**: Three-dimensional schema representation
- **Animation**: Smooth transitions and animations

### Advanced Features
- **Dependency Analysis**: Show extension-to-extension dependencies
- **Performance Metrics**: Show table sizes and query performance
- **Security Analysis**: Highlight security-related tables
- **Migration Tools**: Help with database migrations

## 📱 Mobile Support

The interface is fully responsive and works on:
- **Desktop**: Full interactive experience
- **Tablet**: Touch-friendly controls
- **Mobile**: Simplified view with essential features

## 🎨 Color Scheme

- **💖 Core LNbits**: #FF1493 (LNbits Pink)
- **🟡 Onchain Features**: #FFD700 (Yellow)
- **🟣 Nostr Integration**: #6600CC (Violet)
- **🔴 Gaming & Entertainment**: #8A0000 (Dark Maroon)
- **🟠 E-commerce & Business**: #CA6702 (Burnt Orange)
- **🔵 Hardware & IoT**: #1A202C (Dark Blue)
- **🟢 Communication & Social**: #0A9396 (Medium Teal)

## 🚀 Deployment

### GitHub Pages (Recommended)
1. Fork this repository
2. Go to Settings → Pages
3. Select "Deploy from a branch" → main
4. Your site will be live at `https://yourusername.github.io/LNbits_TableTown/`

### Local Development
```bash
# Clone the repository
git clone https://github.com/arbadacarbaYK/LNbits_TableTown.git

# Open the HTML file in your browser
open index.html
```

### Self-Hosting
Simply upload `index.html` to any web server - it's completely self-contained!

## 🤝 Contributing

To contribute to this project:
1. Fork the repository
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For support or questions:
- **GitHub Issues**: [Report bugs or request features](https://github.com/arbadacarbaYK/LNbits_TableTown/issues)
- **Email**: [info@plebtag.com](mailto:info@plebtag.com)
- **GitHub**: [@arbadacarbayk](https://github.com/arbadacarbaYK)
- **Community**: Join the LNbits community for help

---

**Enjoy exploring the LNbits database schema! 🚀**
