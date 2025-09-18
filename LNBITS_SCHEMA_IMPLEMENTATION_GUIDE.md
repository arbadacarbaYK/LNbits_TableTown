# LNbits Database Schema Implementation Guide

## How to Generate the Complete Database Schema

### Method 1: Using LNbits Codebase Analysis (Recommended)

#### Step 1: Clone the Repositories
```bash
# Clone core LNbits
git clone https://github.com/lnbits/lnbits.git
cd lnbits

# Clone extensions you want to analyze
git clone https://github.com/lnbits/lnurlp.git
git clone https://github.com/lnbits/boltcards.git
git clone https://github.com/lnbits/lnurlw.git
```

#### Step 2: Extract Database Models
```bash
# Core models are in lnbits/core/models/
ls lnbits/core/models/
# Output: users.py, wallets.py, payments.py, extensions.py, etc.

# Extension models are in each extension's root directory
ls lnurlp/models.py
ls boltcards/models.py
ls lnurlw/models.py
```

#### Step 3: Generate Schema Using Python Tools
```python
# Install required packages
pip install sqlalchemy eralchemy graphviz

# Create a script to extract models
from sqlalchemy import create_engine, MetaData
from eralchemy import render_er

# Connect to your LNbits database (if you have one running)
engine = create_engine('sqlite:///lnbits.db')
metadata = MetaData()
metadata.reflect(bind=engine)

# Generate ER diagram
render_er(metadata, 'lnbits_schema.png')
```

### Method 2: Using Database Visualization Tools

#### Option A: DbSchema (Professional Tool)
1. Download DbSchema from [dbschema.com](https://www.dbschema.com/)
2. Connect to your LNbits database
3. Use reverse engineering to extract schema
4. Apply color coding:
   - **Blue**: Core admin tables
   - **Green**: Core user tables
   - **Red**: LNURLp extension
   - **Orange**: Boltcards extension
   - **Purple**: LNURLw extension

#### Option B: ChartDB (Online Tool)
1. Visit [chartdb.io](https://chartdb.io/)
2. Connect to your database
3. Generate automatic schema visualization
4. Export as PNG/SVG for documentation

#### Option C: dbdiagram.io (Free Online)
1. Visit [dbdiagram.io](https://dbdiagram.io/)
2. Create new diagram
3. Manually input table definitions based on models.py files
4. Use color coding for different categories

### Method 3: Using Swagger/OpenAPI Analysis

#### Step 1: Start LNbits Instance
```bash
cd lnbits
poetry install
poetry run lnbits
```

#### Step 2: Access Swagger Documentation
- Navigate to `http://localhost:5000/docs`
- Review API endpoints and data models
- Note: This shows API models, not database schema directly

#### Step 3: Extract Schema Information
- API models give insights into data structure
- Cross-reference with models.py files for complete picture

## Complete Extension Analysis

### LNURLp Extension ([github.com/lnbits/lnurlp](https://github.com/lnbits/lnurlp))

**Purpose**: Static payment links and Lightning Addresses

**Key Tables**:
- `PayLink`: Main table for payment links
- `LnurlpSettings`: Extension configuration

**Integration Points**:
- References `Wallet.id` for wallet association
- Creates entries in core `Payment` table

### Boltcards Extension ([github.com/lnbits/boltcards](https://github.com/lnbits/boltcards))

**Purpose**: NFC card payments using NXP NTAG424

**Key Features**:
- Card management
- Payment processing
- NFC integration

**Integration Points**:
- Wallet-based payments
- Core payment tracking

### LNURLw Extension ([github.com/lnbits/lnurlw](https://github.com/lnbits/lnurlw))

**Purpose**: Withdraw functionality

**Key Features**:
- Withdraw links
- Amount limits
- User authentication

**Integration Points**:
- Wallet withdrawals
- Payment processing

## Database Schema Categories

### 🔵 Core Admin/System Tables
- **Account**: User management and authentication
- **AccessControlList**: API access control
- **UserAcls**: User-specific access controls
- **Extensions**: Extension management
- **Audit**: System audit trails

### 🟢 Core User Data Tables
- **Wallet**: Lightning wallet management
- **Payment**: Payment transaction records
- **Notifications**: User notifications
- **TinyURL**: URL shortening service

### 🟡 Core System/Node Tables
- **LNURL**: LNURL service management
- **WebPush**: Web push notifications
- **Misc**: Miscellaneous system data

### 🔴 Extension Tables (Color Coded by Extension)
- **LNURLp**: Pay link extension tables
- **Boltcards**: NFC card extension tables
- **LNURLw**: Withdraw extension tables
- **Other Extensions**: Additional extension tables

## Foreign Key Relationships

### Core Relationships
```
Account (1) → (N) Wallet
Wallet (1) → (N) Payment
Wallet (1) → (N) PayLink [LNURLp]
Wallet (1) → (N) WithdrawLink [LNURLw]
```

### Extension Relationships
```
PayLink.wallet → Wallet.id
WithdrawLink.wallet → Wallet.id
BoltCard.wallet → Wallet.id
```

## Implementation Best Practices

### 1. Schema Documentation
- Document all tables with their purpose
- Include field descriptions and constraints
- Note foreign key relationships
- Document extension integration points

### 2. Color Coding Strategy
- Use consistent colors across all diagrams
- Group related tables visually
- Highlight extension boundaries
- Use legends for clarity

### 3. Version Control
- Keep schema diagrams in version control
- Update diagrams when schema changes
- Tag releases with schema versions
- Document migration paths

### 4. Extension Development
- Follow LNbits extension patterns
- Reference core tables appropriately
- Don't modify core schema directly
- Use proper foreign key relationships

## Tools Comparison

| Tool | Cost | Features | Best For |
|------|------|----------|----------|
| DbSchema | Paid | Professional, Color coding, Documentation | Production use |
| ChartDB | Freemium | Online, Collaboration, Real-time | Team collaboration |
| dbdiagram.io | Free | Simple, Online, Export | Quick diagrams |
| SchemaSpy | Free | Open source, HTML docs | Documentation |
| ERAlchemy | Free | Python-based, Automated | Development |

## Next Steps

1. **Complete Extension Analysis**: Extract models from all extensions
2. **Create Visual Diagrams**: Use recommended tools
3. **Document Relationships**: Detail all foreign keys
4. **Maintain Documentation**: Keep schema docs updated
5. **Extension Registry**: Create comprehensive extension catalog

## Resources

- [LNbits Core Repository](https://github.com/lnbits/lnbits)
- [LNbits Extensions Registry](https://github.com/lnbits/lnbits-extensions)
- [LNbits Documentation](https://docs.lnbits.org/)
- [LNbits Extensions Wiki](https://github.com/lnbits/lnbits/wiki/LNbits-Extensions)
- [DbSchema Documentation](https://www.dbschema.com/documentation/)
- [ChartDB Documentation](https://chartdb.io/docs/)

---

*This guide provides multiple approaches to generate comprehensive LNbits database schema visualizations. Choose the method that best fits your needs and resources.*
