# LNbits Database Schema - Visual Diagram

## Entity Relationship Diagram

```mermaid
erDiagram
    %% Core Tables - Admin/System (Blue)
    Account {
        string id PK
        string external_id
        string username
        string password_hash
        string pubkey
        string email
        UserExtra extra
        datetime created_at
        datetime updated_at
        boolean is_super_user
        boolean is_admin
        list fiat_providers
    }
    
    AccessControlList {
        string id PK
        string name
        list endpoints
        list token_id_list
    }
    
    UserAcls {
        string id PK
        list access_control_list
        datetime updated_at
    }
    
    %% Core Tables - User Data (Green)
    Wallet {
        string id PK
        string user FK
        string name
        string adminkey
        string inkey
        boolean deleted
        datetime created_at
        datetime updated_at
        string currency
        int balance_msat
        WalletExtra extra
    }
    
    Payment {
        string checking_id PK
        string payment_hash
        string wallet_id FK
        int amount
        int fee
        string bolt11
        string fiat_provider
        string status
        string memo
        datetime expiry
        string webhook
        string webhook_status
        string preimage
        string tag
        string extension
        datetime time
        datetime created_at
        datetime updated_at
        dict extra
    }
    
    %% LNURLp Extension Tables (Red)
    PayLink {
        string id PK
        string wallet FK
        string description
        float min
        float max
        int served_meta
        int served_pr
        int comment_chars
        datetime created_at
        datetime updated_at
        string username
        boolean zaps
        string webhook_url
        string webhook_headers
        string webhook_body
        string success_text
        string success_url
        string currency
        int fiat_base_multiplier
        boolean disposable
        string domain
    }
    
    LnurlpSettings {
        string nostr_private_key
    }
    
    %% Relationships
    Account ||--o{ Wallet : "owns"
    Wallet ||--o{ Payment : "contains"
    Wallet ||--o{ PayLink : "creates"
    
    %% Extension Relationships
    PayLink }o--|| Wallet : "belongs to"
    Payment }o--|| Wallet : "belongs to"
```

## Table Categories Legend

### 🔵 Core Admin/System Tables
- **Account**: User account management
- **AccessControlList**: API access control
- **UserAcls**: User access control lists

### 🟢 Core User Data Tables  
- **Wallet**: Lightning wallet management
- **Payment**: Payment transaction records

### 🔴 LNURLp Extension Tables
- **PayLink**: Static payment links and Lightning Addresses
- **LnurlpSettings**: Extension configuration

## Key Relationships

1. **Account → Wallet**: One-to-Many (User owns multiple wallets)
2. **Wallet → Payment**: One-to-Many (Wallet contains multiple payments)
3. **Wallet → PayLink**: One-to-Many (Wallet can create multiple pay links)

## Extension Integration Points

- **LNURLp Extension**: Integrates with core `Wallet` table to create payment links
- **Payment Tracking**: All extensions can create entries in the core `Payment` table
- **User Context**: Extensions operate within the user context established by `Account` table

## Database Features

- **Soft Deletes**: Uses `deleted` flags instead of hard deletes
- **Audit Trails**: `created_at` and `updated_at` timestamps on all tables
- **Webhook Support**: Built-in webhook functionality for payments
- **Multi-Currency**: Support for various currencies and fiat providers
- **Nostr Integration**: Support for Nostr zaps in LNURLp extension

## Color Coding for Visual Tools

When using database visualization tools like DbSchema or ChartDB, use this color scheme:

- **🔵 Blue (#0066CC)**: Core admin/system tables
- **🟢 Green (#00AA44)**: Core user data tables  
- **🟡 Yellow (#FFAA00)**: Core system/node tables
- **🔴 Red (#CC0000)**: LNURLp extension tables
- **🟠 Orange (#FF6600)**: Boltcards extension tables
- **🟣 Purple (#6600CC)**: LNURLw extension tables
- **⚫ Black (#333333)**: Other extension tables

## Implementation Notes

- **Primary Keys**: All tables use string-based UUIDs as primary keys
- **Foreign Keys**: Clear relationships between core and extension tables
- **Extensibility**: Extension tables reference core tables but don't modify them
- **Data Integrity**: Soft deletes and audit trails maintain data integrity
- **Scalability**: Modular design allows for easy addition of new extensions
