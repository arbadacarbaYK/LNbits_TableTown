# LNbits Table Town 🏘️

**Interactive Database Explorer for LNbits**

## 🎯 Overview

LNbits Table Town is an interactive database schema visualization that provides a comprehensive, zoomable, and filterable view of the LNbits database structure, including all extensions. It's designed for both developers and end-users to understand the LNbits ecosystem.

**Live Demo**: [https://arbadacarbayk.github.io/LNbits_TableTown/](https://arbadacarbayk.github.io/LNbits_TableTown/)

<img height="250" alt="Screenshot from 2025-09-18 13-47-29" src="https://github.com/user-attachments/assets/22ac3b92-7cf2-4ca1-8bad-0f721d8147ce" />

## 🚀 Features

### 🎯 Interactive Table Exploration
Click any table (core or extension) to see detailed dependency information and highlight related tables.

<img height="200" alt="Interactive table highlighting" src="https://github.com/user-attachments/assets/a3b718a0-92e3-4010-9221-4e8bfd66370b" />

### 📊 Dependency Analysis Modal
When you click a table, a modal appears showing:
- **📥 Uses Data From**: Which tables this table reads data from
- **📤 Provides Data To**: Which tables use data from this table  
- **🔗 Foreign Key Fields**: Specific field relationships (e.g., `user → account.id`)

<img height="200" alt="Dependency analysis modal" src="https://github.com/user-attachments/assets/293dcfd3-18c9-41f7-8321-03f89c005b1b" />

### 📖 Comprehensive Legend
Detailed explanations of all abbreviations, data types, and field formats with examples.

<img height="250" alt="Legend with explanations" src="https://github.com/user-attachments/assets/0841023d-b93f-41f5-b56c-76e2e7f5f259" />

### 🔍 Smart Search & Filtering
Real-time search with highlighted results and category-based filtering.

<img height="250" alt="Search functionality" src="https://github.com/user-attachments/assets/2dbf583c-cc8b-4980-bb49-9a7b7359d89d" />

### 📸 Export & Print Features
- **Export View**: Download current view as PNG image
- **Print View**: Generate print-optimized documentation
- **SVG Fallback**: Automatic fallback to SVG if PNG export fails


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
- **All Extensions**: Complete database models for all vetted extensions
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
open index.html
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
- **Click any Table**: See detailed dependency information in modal
- **Highlight Related Tables**: Both core and extension tables highlight
- **Bidirectional Relationships**: Shows both "uses data from" and "provides data to"
- **Foreign Key Details**: See specific field relationships (e.g., `user → account.id`)
- **Click Empty Space**: Reset all highlights and close modal

### 6. **Export & Print**
- **Export View**: Click "📸 Export View" to download PNG image
- **Print View**: Click "🖨️ Print View" for print-optimized documentation
- **SVG Fallback**: Automatic fallback if PNG export fails

## 🛠️ Technical Details

### Data Structure
The `lnbits_extensions_data.json` file contains:
- **Core Tables**: Complete definitions with fields and relationships
- **Extensions**: All vetted extensions with their database models
- **Categories**: Color coding and descriptions for each category
- **Dependencies**: Which extensions depend on core tables

### Technologies Used
- **D3.js**: Interactive visualizations and zoom/pan functionality
- **SVG**: Scalable vector graphics for crisp rendering
- **CSS Grid**: Responsive layout management
- **JavaScript**: Interactive filtering and search

## 🚀 Future Enhancements

### ✅ Completed Features
- **✅ Export Functionality**: Export filtered views as PNG images
- **✅ Print Support**: Generate print-optimized documentation
- **✅ Dependency Analysis**: Interactive table-to-table dependency analysis
- **✅ Bidirectional Relationships**: Shows both directions of data flow
- **✅ Foreign Key Mapping**: Detailed field relationship information

### 🔮 Planned Features
- **API Integration**: Real-time data from LNbits instances
- **3D Visualization**: Three-dimensional schema representation
- **Animation**: Smooth transitions and animations
- **Performance Metrics**: Show table sizes and query performance
- **Security Analysis**: Highlight security-related tables
- **Migration Tools**: Help with database migrations

## 📱 Mobile Support

The interface is fully responsive and works on:
- **Desktop**: Full interactive experience
- **Tablet**: Touch-friendly controls
- **Mobile**: Simplified view with essential features

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For support or questions:
- **Tip the author** : LNURL1DP68GURN8GHJ7CN5D9CZUMNV9UH8WETVDSKKKMN0WAHZ7MRWW4EXCUP0X9UXGDEEXQ6XVVM9XUMXGDFCXY6NQS43TRV
- **GitHub Issues**: [Report bugs or request features](https://github.com/arbadacarbaYK/LNbits_TableTown/issues)
- **Community**: Join the [LNbits community](https://t.me/lnbits) for help

---

**Enjoy exploring the LNbits database schema! 🚀**
