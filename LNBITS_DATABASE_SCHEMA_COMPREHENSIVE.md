# LNbits Database Schema Analysis

## Overview

This document provides a comprehensive analysis of the LNbits database schema, including core tables and extension-specific tables. LNbits is a free and open-source Lightning wallet and accounts system that uses a modular architecture with extensions.

## Core LNbits Database Schema

Based on analysis of the [LNbits core repository](https://github.com/lnbits/lnbits), the main database models are located in `lnbits/core/models/`. Here are the key tables:

### 🔵 Core Tables (Admin/System)

#### 1. **Account** (User Management)
- `id` (str) - Primary Key, UUID4 hex string
- `external_id` (str, optional) - For external account linking
- `username` (str, optional) - User's username
- `password_hash` (str, optional) - Bcrypt hashed password
- `pubkey` (str, optional) - User's public key
- `email` (str, optional) - User's email address
- `extra` (UserExtra) - Additional user metadata
- `created_at` (datetime) - Account creation timestamp
- `updated_at` (datetime) - Last update timestamp
- `is_super_user` (bool) - Super user flag
- `is_admin` (bool) - Admin user flag
- `fiat_providers` (list[str]) - Available fiat providers

#### 2. **AccessControlList** (API Access Control)
- `id` (str) - Primary Key
- `name` (str) - ACL name
- `endpoints` (list[EndpointAccess]) - Allowed endpoints
- `token_id_list` (list[SimpleItem]) - Associated tokens

#### 3. **UserAcls** (User Access Control)
- `id` (str) - Primary Key
- `access_control_list` (list[AccessControlList]) - User's ACLs
- `updated_at` (datetime) - Last update timestamp

### 🟢 Core Tables (User Data)

#### 4. **Wallet** (Wallet Management)
- `id` (str) - Primary Key
- `user` (str) - **FK to Account.id**
- `name` (str) - Wallet name
- `adminkey` (str) - Admin key for wallet operations
- `inkey` (str) - Invoice key for receiving payments
- `deleted` (bool) - Soft delete flag
- `created_at` (datetime) - Creation timestamp
- `updated_at` (datetime) - Last update timestamp
- `currency` (str, optional) - Wallet currency
- `balance_msat` (int) - Balance in millisatoshis
- `extra` (WalletExtra) - Additional wallet metadata

#### 5. **Payment** (Payment Records)
- `checking_id` (str) - Primary Key, unique payment identifier
- `payment_hash` (str) - Lightning payment hash
- `wallet_id` (str) - **FK to Wallet.id**
- `amount` (int) - Payment amount in millisatoshis
- `fee` (int) - Payment fee
- `bolt11` (str) - BOLT11 invoice string
- `fiat_provider` (str, optional) - Fiat payment provider
- `status` (str) - Payment status (pending/success/failed)
- `memo` (str, optional) - Payment memo
- `expiry` (datetime, optional) - Payment expiry
- `webhook` (str, optional) - Webhook URL
- `webhook_status` (str, optional) - Webhook status
- `preimage` (str, optional) - Payment preimage
- `tag` (str, optional) - Payment tag
- `extension` (str, optional) - Source extension
- `time` (datetime) - Payment timestamp
- `created_at` (datetime) - Record creation
- `updated_at` (datetime) - Last update
- `extra` (dict) - Additional payment data

### 🟡 Core Tables (System/Node)

#### 6. **Extensions** (Extension Management)
- Extension-related tables for managing LNbits extensions

#### 7. **Notifications** (System Notifications)
- Notification system tables

#### 8. **Audit** (Audit Logging)
- Audit trail tables for system events

## Extension Database Schemas

### 🔴 LNURLp Extension ([github.com/lnbits/lnurlp](https://github.com/lnbits/lnurlp))

The LNURLp extension enables static QR codes and Lightning Addresses for payments.

#### **PayLink** (Pay Link Management)
- `id` (str) - Primary Key
- `wallet` (str) - **FK to Wallet.id**
- `description` (str) - Link description
- `min` (float) - Minimum payment amount
- `max` (float) - Maximum payment amount
- `served_meta` (int) - Metadata served count
- `served_pr` (int) - Payment requests served count
- `comment_chars` (int) - Allowed comment characters
- `created_at` (datetime) - Creation timestamp
- `updated_at` (datetime) - Last update timestamp
- `username` (str, optional) - Lightning Address username
- `zaps` (bool, optional) - Nostr zaps enabled
- `webhook_url` (str, optional) - Webhook URL
- `webhook_headers` (str, optional) - Webhook headers
- `webhook_body` (str, optional) - Webhook body
- `success_text` (str, optional) - Success message
- `success_url` (str, optional) - Success redirect URL
- `currency` (str, optional) - Payment currency
- `fiat_base_multiplier` (int, optional) - Fiat conversion multiplier
- `disposable` (bool) - Disposable link flag
- `domain` (str, optional) - Domain for Lightning Address

#### **LnurlpSettings** (Extension Settings)
- `nostr_private_key` (str) - Nostr private key for zaps

### 🟠 Boltcards Extension ([github.com/lnbits/boltcards](https://github.com/lnbits/boltcards))

The Boltcards extension enables NFC card payments using NXP NTAG424 cards.

*Note: Specific database models need to be extracted from the boltcards repository*

### 🟣 LNURLw Extension ([github.com/lnbits/lnurlw](https://github.com/lnbits/lnurlw))

The LNURLw extension enables withdraw functionality.

*Note: Specific database models need to be extracted from the lnurlw repository*

## Database Relationships

### Foreign Key Relationships

1. **Wallet → Account**: `Wallet.user` → `Account.id`
2. **Payment → Wallet**: `Payment.wallet_id` → `Wallet.id`
3. **PayLink → Wallet**: `PayLink.wallet` → `Wallet.id`

### Table Categories

- **🔵 Admin/System**: Core system management tables
- **🟢 User Data**: User-specific data and wallets
- **🟡 System/Node**: System-level functionality
- **🔴 LNURLp**: Pay link extension tables
- **🟠 Boltcards**: NFC card payment extension tables
- **🟣 LNURLw**: Withdraw extension tables

## Extension Interactions

### How Extensions Interact with Core

1. **Wallet Integration**: All extensions reference the core `Wallet` table
2. **Payment Tracking**: Extensions can create payments that reference core `Payment` table
3. **User Context**: Extensions operate within the user context established by core `Account` table

### Extension-to-Extension Interactions

1. **Shared Wallet Access**: Multiple extensions can operate on the same wallet
2. **Payment Flow**: Extensions can trigger payments that other extensions can process
3. **User Metadata**: Extensions can share user preferences and settings

## Database Schema Visualization Tools

### Recommended Tools

1. **[DbSchema](https://www.dbschema.com/)**: Professional database design tool with color-coding support
2. **[ChartDB](https://chartdb.io/)**: Online database visualization with collaboration features
3. **[dbdiagram.io](https://dbdiagram.io/)**: Free online database diagram tool
4. **[SchemaSpy](http://schemaspy.org/)**: Open-source database documentation tool

### Color Coding Strategy

- **🔵 Blue**: Core admin/system tables
- **🟢 Green**: Core user data tables
- **🟡 Yellow**: Core system/node tables
- **🔴 Red**: LNURLp extension tables
- **🟠 Orange**: Boltcards extension tables
- **🟣 Purple**: LNURLw extension tables
- **⚫ Black**: Other extension tables

## Implementation Notes

### Database Types Supported
- SQLite (default)
- PostgreSQL
- MySQL

### Key Features
- Soft deletes (deleted flags)
- Audit trails
- Webhook support
- Multi-currency support
- Fiat integration
- Nostr integration (zaps)

## Next Steps

1. **Extract Additional Extension Models**: Complete the analysis for boltcards, lnurlw, and other extensions
2. **Create Visual Diagrams**: Use the recommended tools to create comprehensive ER diagrams
3. **Document Relationships**: Detail all foreign key relationships and constraints
4. **Extension Registry**: Maintain a registry of all available extensions and their schemas

## References

- [LNbits Core Repository](https://github.com/lnbits/lnbits)
- [LNbits Extensions Registry](https://github.com/lnbits/lnbits-extensions)
- [LNURLp Extension](https://github.com/lnbits/lnurlp)
- [LNbits Documentation](https://docs.lnbits.org/)
- [LNbits Extensions Wiki](https://github.com/lnbits/lnbits/wiki/LNbits-Extensions)

---

*This analysis is based on the latest release of LNbits and its extensions as of 2025. For the most up-to-date information, please refer to the official repositories.*
