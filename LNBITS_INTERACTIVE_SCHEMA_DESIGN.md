# LNbits Interactive Database Schema - Enhanced Design

## 🎯 Core Concept Enhancement

### Interactive Web Interface Features

#### 1. **Multi-Level Filtering System**
```
┌─ Filter Panel ─────────────────────────────┐
│ 🔍 Search: [________________]              │
│                                             │
│ 📊 By Functionality:                       │
│   ☑️ All Extensions                        │
│   ☐ Onchain Features (SatsPay, Boltz...)  │
│   ☐ Nostr Integration (Market, Relay...)   │
│   ☐ Gaming & Entertainment                 │
│   ☐ E-commerce & Business                  │
│   ☐ Hardware & IoT                         │
│   ☐ Communication & Social                 │
│                                             │
│ 🎯 By User Type:                           │
│   ☑️ Developer View                        │
│   ☐ End-User View                          │
│                                             │
│ 🔗 Show Dependencies:                      │
│   ☑️ Always show core tables               │
│   ☑️ Highlight extension relationships     │
└─────────────────────────────────────────────┘
```

#### 2. **Visual Design System**

**Color Coding:**
- 🔵 **Core LNbits**: Blue (#0066CC) - Always visible
- 🟢 **Payment Extensions**: Green (#00AA44) - LNURLp, Withdraw, etc.
- 🟠 **Onchain Features**: Orange (#FF6600) - SatsPay, Boltz, WatchOnly
- 🟣 **Nostr Integration**: Purple (#6600CC) - Market, Relay, Client
- 🟡 **Gaming**: Yellow (#FFAA00) - SatsDice, Coinflip, Numbers
- 🔴 **E-commerce**: Red (#CC0000) - Events, Invoices, Paywall
- ⚫ **Hardware/IoT**: Black (#333333) - BitcoinSwitch, LNURLDevice
- 🟤 **Communication**: Brown (#8B4513) - TipJar, StreamAlerts, SMTP

**Visual States:**
- **Active**: Full color and opacity
- **Selected**: Highlighted with border
- **Dependent**: Connected with colored lines
- **Greyed Out**: 30% opacity when filtered out
- **Core Tables**: Always visible, grey background

## 📊 Comprehensive Extension Categorization

### 🔵 Core LNbits Tables (Always Visible)
```
Account (Users & Authentication)
├── Wallet (Lightning Wallets)
├── Payment (Transaction Records)
├── AccessControlList (API Permissions)
└── UserAcls (User Permissions)
```

### 🟠 Onchain Features
**Primary Extensions:**
- **SatsPay** - Onchain and Lightning charges
- **Boltz** - Onchain/offchain swaps with Liquid support
- **WatchOnly** - Onchain watch-only wallets
- **SellCoins** - Sell coins for fiat

**Dependencies:** All connect to core `Wallet` table

### 🟣 Nostr Integration
**Primary Extensions:**
- **NostrMarket** - Nostr marketplace/webshop
- **NostrRelay** - One-click relay management
- **NostrClient** - Nostr client for extensions
- **NostrNip5** - NIP-5 address verification

**Dependencies:** 
- Connect to core `Wallet` for payments
- May have cross-extension dependencies

### 🟡 Gaming & Entertainment
**Primary Extensions:**
- **SatsDice** - LNURL Satoshi dice games
- **Coinflip** - Bet sats on coinflips
- **Numbers** - Block-based numbers game
- **Eightball** - Magic 8ball with payments
- **Satspot** - Money pool games
- **Jukebox** - Spotify jukebox with sats

**Dependencies:** All use core `Payment` table

### 🔴 E-commerce & Business
**Primary Extensions:**
- **Events** - Event ticket sales
- **Invoices** - Invoice creation for clients
- **Paywall** - Content paywalls
- **OfflineShop** - Offline product payments
- **Subdomains** - Subdomain sales
- **LNAddress** - Lightning Address sales
- **AuctionHouse** - Digital goods auctions

**Dependencies:** 
- Core `Wallet` and `Payment` tables
- May integrate with each other

### ⚫ Hardware & IoT
**Primary Extensions:**
- **BitcoinSwitch** - Turn things on with bitcoin
- **LNURLDevice** - IoT device control
- **Bleskomat** - ATM integration
- **FOSSA** - DIY Bitcoin ATM
- **LNPoS** - Lightning point of sale

**Dependencies:** Core `Wallet` for payment processing

### 🟤 Communication & Social
**Primary Extensions:**
- **TipJar** - Bitcoin donations with messages
- **StreamAlerts** - Stream donation alerts
- **Copilot** - Streamer tools and animations
- **SMTP** - Email service for sats
- **DiscordBot** - Discord integration

**Dependencies:** Core `Payment` and `Wallet` tables

### 🟢 Core Payment Extensions
**Primary Extensions:**
- **LNURLp** - Static payment links
- **Withdraw** - LNURL withdraw links
- **Boltcards** - NFC card payments
- **TPoS** - Point of sale terminal
- **SplitPayments** - Payment splitting

**Dependencies:** Core `Wallet` table (primary)

## 🎮 Interactive Features

### 1. **Smart Filtering**
```javascript
// Example filter logic
function filterByCategory(category) {
    if (category === 'onchain') {
        showExtensions(['satspay', 'boltz', 'watchonly', 'sellcoins']);
        highlightCoreTables(['wallet', 'payment']);
        greyOutOthers();
    }
}
```

### 2. **Dependency Visualization**
- **Solid Lines**: Direct foreign key relationships
- **Dashed Lines**: Extension-to-extension dependencies
- **Thick Lines**: Critical dependencies
- **Animated**: Show data flow on hover

### 3. **User-Friendly Descriptions**
```html
<div class="tooltip">
    <h3>SatsPay Extension</h3>
    <p><strong>For End Users:</strong> Accept Bitcoin payments on your website or app</p>
    <p><strong>For Developers:</strong> Creates onchain and Lightning invoices</p>
    <p><strong>Tables:</strong> SatsPayCharge, SatsPayPayment</p>
    <p><strong>Dependencies:</strong> Core Wallet table</p>
</div>
```

### 4. **Zoom Levels**
- **Overview**: All tables, small size
- **Category View**: Filtered extensions + core
- **Detail View**: Single extension + dependencies
- **Table Detail**: Individual table structure

## 🛠️ Technical Implementation

### Frontend Technologies
- **D3.js**: For interactive visualizations
- **SVG**: Scalable vector graphics
- **CSS Grid**: Layout management
- **JavaScript**: Interactive filtering

### Data Structure
```json
{
  "extensions": {
    "satspay": {
      "name": "SatsPay Server",
      "category": "onchain",
      "tables": ["SatsPayCharge", "SatsPayPayment"],
      "dependencies": ["wallet"],
      "description": {
        "end_user": "Accept Bitcoin payments on your website",
        "developer": "Creates onchain and Lightning invoices"
      }
    }
  }
}
```

### Responsive Design
- **Desktop**: Full interactive experience
- **Tablet**: Touch-friendly controls
- **Mobile**: Simplified view with essential features

## 🎯 User Experience Enhancements

### For Developers
- **Technical Details**: Table schemas, foreign keys, indexes
- **API Endpoints**: Available endpoints for each extension
- **Code Examples**: Sample queries and integrations

### For End Users
- **Plain English**: What each extension does
- **Use Cases**: Real-world applications
- **Setup Guides**: How to enable and configure

### For Both
- **Search Functionality**: Find anything quickly
- **Export Options**: Save filtered views
- **Print Friendly**: Generate documentation

## 🚀 Implementation Plan

1. **Phase 1**: Create basic interactive interface
2. **Phase 2**: Add all extension data and categorization
3. **Phase 3**: Implement advanced filtering and dependencies
4. **Phase 4**: Add user-friendly descriptions and tooltips
5. **Phase 5**: Optimize for mobile and accessibility

This enhanced design creates a comprehensive, interactive database schema that serves both technical developers and non-technical users, making LNbits' complex architecture accessible and understandable to everyone.
