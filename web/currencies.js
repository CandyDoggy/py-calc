// Currency Data and Converter
const CURRENCY_RATES = {
    USD: 1.0, EUR: 0.92, GBP: 0.79, JPY: 149.50, CNY: 7.24,
    AUD: 1.53, CAD: 1.36, CHF: 0.88, INR: 83.12, KRW: 1325.0,
    MXN: 17.15, BRL: 4.97, SGD: 1.34, HKD: 7.82, NZD: 1.64,
    SEK: 10.45, NOK: 10.62, TRY: 30.25, RUB: 92.50, ZAR: 18.95,
    AMD: 403.50, DRAM: 403.50, AED: 3.67, THB: 35.20, IDR: 15650.0,
    MYR: 4.72, PHP: 55.80, PLN: 4.02, CZK: 22.85, HUF: 355.0,
    ILS: 3.65, CLP: 890.0, COP: 3950.0, ARS: 350.0, EGP: 30.90,
    SAR: 3.75, QAR: 3.64, KWD: 0.31, BHD: 0.38, OMR: 0.38,
    JOD: 0.71, LKR: 325.0, PKR: 278.0, BDT: 109.50, VND: 24350.0,
    NGN: 770.0, KES: 155.0, GHS: 12.05, UAH: 36.80, RON: 4.57,
    BGN: 1.80, HRK: 6.93, DKK: 6.87, ISK: 137.50
};

const CURRENCY_SYMBOLS = {
    USD: '$', EUR: '€', GBP: '£', JPY: '¥', CNY: '¥',
    AUD: 'A$', CAD: 'C$', CHF: 'Fr', INR: '₹', KRW: '₩',
    MXN: 'MX$', BRL: 'R$', SGD: 'S$', HKD: 'HK$', NZD: 'NZ$',
    SEK: 'kr', NOK: 'kr', TRY: '₺', RUB: '₽', ZAR: 'R',
    AMD: '֏', DRAM: '֏', AED: 'د.إ', THB: '฿', IDR: 'Rp', MYR: 'RM',
    PHP: '₱', PLN: 'zł', CZK: 'Kč', HUF: 'Ft', ILS: '₪',
    CLP: 'CL$', COP: 'CO$', ARS: 'AR$', EGP: 'E£', SAR: '﷼',
    QAR: '﷼', KWD: 'KD', BHD: 'BD', OMR: '﷼', JOD: 'JD',
    LKR: '₨', PKR: '₨', BDT: '৳', VND: '₫', NGN: '₦',
    KES: 'KSh', GHS: '₵', UAH: '₴', RON: 'lei', BGN: 'лв',
    HRK: 'kn', DKK: 'kr', ISK: 'kr'
};

const CURRENCY_NAMES = {
    USD: 'US Dollar', EUR: 'Euro', GBP: 'British Pound', JPY: 'Japanese Yen',
    CNY: 'Chinese Yuan', AUD: 'Australian Dollar', CAD: 'Canadian Dollar',
    CHF: 'Swiss Franc', INR: 'Indian Rupee', KRW: 'South Korean Won',
    MXN: 'Mexican Peso', BRL: 'Brazilian Real', SGD: 'Singapore Dollar',
    HKD: 'Hong Kong Dollar', NZD: 'New Zealand Dollar', SEK: 'Swedish Krona',
    NOK: 'Norwegian Krone', TRY: 'Turkish Lira', RUB: 'Russian Ruble',
    ZAR: 'South African Rand', AMD: 'Armenian Dram', DRAM: 'Armenian Dram',
    AED: 'UAE Dirham', THB: 'Thai Baht', IDR: 'Indonesian Rupiah',
    MYR: 'Malaysian Ringgit', PHP: 'Philippine Peso', PLN: 'Polish Zloty',
    CZK: 'Czech Koruna', HUF: 'Hungarian Forint', ILS: 'Israeli Shekel',
    CLP: 'Chilean Peso', COP: 'Colombian Peso', ARS: 'Argentine Peso',
    EGP: 'Egyptian Pound', SAR: 'Saudi Riyal', QAR: 'Qatari Riyal',
    KWD: 'Kuwaiti Dinar', BHD: 'Bahraini Dinar', OMR: 'Omani Rial',
    JOD: 'Jordanian Dinar', LKR: 'Sri Lankan Rupee', PKR: 'Pakistani Rupee',
    BDT: 'Bangladeshi Taka', VND: 'Vietnamese Dong', NGN: 'Nigerian Naira',
    KES: 'Kenyan Shilling', GHS: 'Ghanaian Cedi', UAH: 'Ukrainian Hryvnia',
    RON: 'Romanian Leu', BGN: 'Bulgarian Lev', HRK: 'Croatian Kuna',
    DKK: 'Danish Krone', ISK: 'Icelandic Krona'
};

class CurrencyConverter {
    constructor() {
        this.fromCurrency = 'USD';
        this.toCurrency = 'EUR';
        this.amount = 1;
        this.selectMode = 'from'; // 'from' or 'to'
    }

    convert(amount, from, to) {
        const fromRate = CURRENCY_RATES[from];
        const toRate = CURRENCY_RATES[to];
        
        if (!fromRate || !toRate) {
            throw new Error('Invalid currency');
        }

        return amount * (toRate / fromRate);
    }

    formatCurrency(amount, currency) {
        const symbol = CURRENCY_SYMBOLS[currency] || currency;
        return `${symbol}${amount.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    }

    getCurrencyInfo(code) {
        return {
            code: code,
            name: CURRENCY_NAMES[code] || code,
            symbol: CURRENCY_SYMBOLS[code] || code,
            rate: CURRENCY_RATES[code]
        };
    }

    getAllCurrencies() {
        return Object.keys(CURRENCY_RATES)
            .sort((a, b) => a.localeCompare(b))
            .map(code => this.getCurrencyInfo(code));
    }

    filterCurrencies(query) {
        const lowerQuery = query.toLowerCase();
        return this.getAllCurrencies().filter(currency => 
            currency.code.toLowerCase().includes(lowerQuery) ||
            currency.name.toLowerCase().includes(lowerQuery) ||
            currency.symbol.toLowerCase().includes(lowerQuery)
        );
    }

    swap() {
        [this.fromCurrency, this.toCurrency] = [this.toCurrency, this.fromCurrency];
    }
}

// Metric/Imperial Conversion Data
const METRIC_UNITS = {
    length: {
        base: 'm',
        units: {
            'mm': { name: 'Millimeters (mm)', toBase: 0.001 },
            'cm': { name: 'Centimeters (cm)', toBase: 0.01 },
            'm': { name: 'Meters (m)', toBase: 1 },
            'km': { name: 'Kilometers (km)', toBase: 1000 },
            'in': { name: 'Inches (in)', toBase: 0.0254 },
            'ft': { name: 'Feet (ft)', toBase: 0.3048 },
            'yd': { name: 'Yards (yd)', toBase: 0.9144 },
            'mi': { name: 'Miles (mi)', toBase: 1609.344 }
        }
    },
    weight: {
        base: 'kg',
        units: {
            'mg': { name: 'Milligrams (mg)', toBase: 0.000001 },
            'g': { name: 'Grams (g)', toBase: 0.001 },
            'kg': { name: 'Kilograms (kg)', toBase: 1 },
            'oz': { name: 'Ounces (oz)', toBase: 0.0283495 },
            'lb': { name: 'Pounds (lb)', toBase: 0.453592 },
            'st': { name: 'Stone (st)', toBase: 6.35029 },
            'ton': { name: 'US Tons (ton)', toBase: 907.185 }
        }
    },
    volume: {
        base: 'L',
        units: {
            'mL': { name: 'Milliliters (mL)', toBase: 0.001 },
            'L': { name: 'Liters (L)', toBase: 1 },
            'tsp': { name: 'Teaspoons (tsp)', toBase: 0.00492892 },
            'tbsp': { name: 'Tablespoons (tbsp)', toBase: 0.0147868 },
            'fl oz': { name: 'Fluid Ounces (fl oz)', toBase: 0.0295735 },
            'cup': { name: 'Cups', toBase: 0.236588 },
            'pt': { name: 'Pints (pt)', toBase: 0.473176 },
            'qt': { name: 'Quarts (qt)', toBase: 0.946353 },
            'gal': { name: 'Gallons (gal)', toBase: 3.78541 }
        }
    },
    speed: {
        base: 'm/s',
        units: {
            'm/s': { name: 'Meters/second (m/s)', toBase: 1 },
            'km/h': { name: 'Kilometers/hour (km/h)', toBase: 0.277778 },
            'mph': { name: 'Miles/hour (mph)', toBase: 0.44704 },
            'knot': { name: 'Knots', toBase: 0.514444 },
            'ft/s': { name: 'Feet/second (ft/s)', toBase: 0.3048 }
        }
    },
    area: {
        base: 'm²',
        units: {
            'mm²': { name: 'Square Millimeters (mm²)', toBase: 0.000001 },
            'cm²': { name: 'Square Centimeters (cm²)', toBase: 0.0001 },
            'm²': { name: 'Square Meters (m²)', toBase: 1 },
            'km²': { name: 'Square Kilometers (km²)', toBase: 1000000 },
            'in²': { name: 'Square Inches (in²)', toBase: 0.00064516 },
            'ft²': { name: 'Square Feet (ft²)', toBase: 0.092903 },
            'ac': { name: 'Acres (ac)', toBase: 4046.86 },
            'ha': { name: 'Hectares (ha)', toBase: 10000 }
        }
    },
    time: {
        base: 's',
        units: {
            'ms': { name: 'Milliseconds (ms)', toBase: 0.001 },
            's': { name: 'Seconds (s)', toBase: 1 },
            'min': { name: 'Minutes (min)', toBase: 60 },
            'hr': { name: 'Hours (hr)', toBase: 3600 },
            'day': { name: 'Days', toBase: 86400 },
            'week': { name: 'Weeks', toBase: 604800 },
            'month': { name: 'Months (avg)', toBase: 2629746 },
            'year': { name: 'Years (avg)', toBase: 31556952 }
        }
    },
    data: {
        base: 'B',
        units: {
            'bit': { name: 'Bits', toBase: 0.125 },
            'B': { name: 'Bytes (B)', toBase: 1 },
            'KB': { name: 'Kilobytes (KB)', toBase: 1024 },
            'MB': { name: 'Megabytes (MB)', toBase: 1048576 },
            'GB': { name: 'Gigabytes (GB)', toBase: 1073741824 },
            'TB': { name: 'Terabytes (TB)', toBase: 1099511627776 }
        }
    },
    energy: {
        base: 'J',
        units: {
            'J': { name: 'Joules (J)', toBase: 1 },
            'kJ': { name: 'Kilojoules (kJ)', toBase: 1000 },
            'cal': { name: 'Calories (cal)', toBase: 4.184 },
            'kcal': { name: 'Kilocalories (kcal)', toBase: 4184 },
            'Wh': { name: 'Watt-hours (Wh)', toBase: 3600 },
            'kWh': { name: 'Kilowatt-hours (kWh)', toBase: 3600000 }
        }
    },
    pressure: {
        base: 'Pa',
        units: {
            'Pa': { name: 'Pascals (Pa)', toBase: 1 },
            'kPa': { name: 'Kilopascals (kPa)', toBase: 1000 },
            'bar': { name: 'Bar', toBase: 100000 },
            'psi': { name: 'PSI', toBase: 6894.76 },
            'atm': { name: 'Atmospheres (atm)', toBase: 101325 },
            'mmHg': { name: 'mmHg', toBase: 133.322 }
        }
    }
};

// Temperature conversion (special case - not linear)
function convertTemperature(value, from, to) {
    // Convert to Celsius first
    let celsius;
    switch (from) {
        case 'C': celsius = value; break;
        case 'F': celsius = (value - 32) * 5/9; break;
        case 'K': celsius = value - 273.15; break;
    }

    // Convert from Celsius to target
    switch (to) {
        case 'C': return celsius;
        case 'F': return (celsius * 9/5) + 32;
        case 'K': return celsius + 273.15;
    }
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        CurrencyConverter,
        CURRENCY_RATES,
        CURRENCY_SYMBOLS,
        CURRENCY_NAMES,
        METRIC_UNITS,
        convertTemperature
    };
}
