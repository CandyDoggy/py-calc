// Converter Module for Metric/Imperial and Temperature
class MetricConverter {
    constructor() {
        this.currentType = 'length';
        this.fromUnit = 'm';
        this.toUnit = 'ft';
    }

    setType(type) {
        this.currentType = type;
        const units = METRIC_UNITS[type].units;
        const unitKeys = Object.keys(units);
        this.fromUnit = unitKeys[0];
        this.toUnit = unitKeys[unitKeys.length > 1 ? 1 : 0];
    }

    convert(value, from, to) {
        const typeData = METRIC_UNITS[this.currentType];
        const fromFactor = typeData.units[from].toBase;
        const toFactor = typeData.units[to].toBase;
        
        // Convert to base unit, then to target unit
        const baseValue = value * fromFactor;
        return baseValue / toFactor;
    }

    getUnitName(code) {
        return METRIC_UNITS[this.currentType].units[code].name;
    }

    getAllUnits() {
        return Object.entries(METRIC_UNITS[this.currentType].units).map(([code, data]) => ({
            code,
            name: data.name
        }));
    }
}

class TemperatureConverter {
    static convert(value, from, to) {
        return convertTemperature(value, from, to);
    }

    static celsiusToFahrenheit(c) {
        return (c * 9/5) + 32;
    }

    static fahrenheitToCelsius(f) {
        return (f - 32) * 5/9;
    }

    static celsiusToKelvin(c) {
        return c + 273.15;
    }

    static kelvinToCelsius(k) {
        return k - 273.15;
    }

    static fahrenheitToKelvin(f) {
        const c = this.fahrenheitToCelsius(f);
        return this.celsiusToKelvin(c);
    }

    static kelvinToFahrenheit(k) {
        const c = this.kelvinToCelsius(k);
        return this.celsiusToFahrenheit(c);
    }
}

// Export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { MetricConverter, TemperatureConverter };
}
