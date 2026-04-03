// Main Calculator Application
class CalculatorApp {
    constructor() {
        this.currentMode = 'standard';
        this.currentTheme = 'fluent-dark';
        this.mathEngine = new MathEngine();
        this.currencyConverter = new CurrencyConverter();
        this.metricConverter = new MetricConverter();
        
        // Calculator state
        this.currentExpression = '';
        this.currentResult = '0';
        this.memory = [];
        this.lastResult = 0;
        
        // Programmer mode state
        this.progExpression = '';
        this.progResult = '0';
        
        // Memory
        this.loadMemory();
        this.loadTheme();
        
        this.init();
    }

    init() {
        this.bindEvents();
        this.applyTheme(this.currentTheme);
        this.loadMemoryPanelState();
        this.switchMode('standard');
        this.buildCurrencyList();
        this.buildMetricUnitList();
        this.updateCurrencyConversion();
        this.updateMetricConversion();
        this.refreshMemoryDisplay();
    }

    bindEvents() {
        // Navigation buttons
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const mode = e.currentTarget.dataset.mode;
                this.switchMode(mode);
            });
        });

        // Theme selector
        document.getElementById('theme-select').addEventListener('change', (e) => {
            this.applyTheme(e.target.value);
            this.saveTheme();
        });

        // Calculator buttons (all modes)
        document.querySelectorAll('.btn, .mem-btn, .min-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const action = e.target.dataset.action;
                this.handleButtonPress(action);
            });
        });

        // Memory panel toggle
        document.getElementById('memory-close-btn').addEventListener('click', () => {
            this.hideMemoryPanel();
        });

        document.getElementById('memory-toggle-btn').addEventListener('click', () => {
            this.showMemoryPanel();
        });

        document.getElementById('memory-clear-btn').addEventListener('click', () => {
            this.clearAllMemory();
        });

        // Currency converter
        document.getElementById('currency-amount').addEventListener('input', () => {
            this.updateCurrencyConversion();
        });

        document.getElementById('swap-currencies').addEventListener('click', () => {
            this.currencyConverter.swap();
            this.updateCurrencyDisplay();
            this.updateCurrencyConversion();
        });

        document.getElementById('currency-search').addEventListener('input', (e) => {
            this.filterCurrencyList(e.target.value);
        });

        document.querySelectorAll('input[name="currency-select-mode"]').forEach(radio => {
            radio.addEventListener('change', (e) => {
                this.currencyConverter.selectMode = e.target.value;
            });
        });

        // Metric converter
        document.getElementById('metric-type').addEventListener('change', (e) => {
            this.metricConverter.setType(e.target.value);
            this.buildMetricUnitList();
            this.updateMetricConversion();
        });

        document.getElementById('metric-from-value').addEventListener('input', () => {
            this.updateMetricConversion();
        });

        document.getElementById('swap-metric').addEventListener('click', () => {
            [this.metricConverter.fromUnit, this.metricConverter.toUnit] = 
            [this.metricConverter.toUnit, this.metricConverter.fromUnit];
            this.updateMetricConversion();
        });

        // Temperature converter
        document.getElementById('temp-celsius').addEventListener('input', (e) => {
            this.updateTemperatureFromCelsius(e.target.value);
        });

        document.getElementById('temp-fahrenheit').addEventListener('input', (e) => {
            this.updateTemperatureFromFahrenheit(e.target.value);
        });

        document.getElementById('temp-kelvin').addEventListener('input', (e) => {
            this.updateTemperatureFromKelvin(e.target.value);
        });

        // Keyboard support
        document.addEventListener('keydown', (e) => {
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
            
            const key = e.key;
            if (/^[0-9.]$/.test(key)) {
                e.preventDefault();
                this.handleButtonPress(key);
            } else if (key === '+' || key === '-' || key === '*' || key === '/') {
                e.preventDefault();
                this.handleButtonPress(key);
            } else if (key === 'Enter' || key === '=') {
                e.preventDefault();
                this.handleButtonPress('=');
            } else if (key === 'Backspace') {
                e.preventDefault();
                this.handleButtonPress('backspace');
            } else if (key === 'Escape' || key === 'c' || key === 'C') {
                e.preventDefault();
                this.handleButtonPress('C');
            } else if (key === '%') {
                e.preventDefault();
                this.handleButtonPress('%');
            } else if (key === '(' || key === ')') {
                e.preventDefault();
                this.handleButtonPress(key);
            } else if (key === '^') {
                e.preventDefault();
                this.handleButtonPress('^');
            }
        });
    }

    switchMode(mode) {
        this.currentMode = mode;
        
        // Update navigation
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });

        // Update mode views
        document.querySelectorAll('.mode-view').forEach(view => {
            view.classList.remove('active');
        });

        const modeView = document.getElementById(`${mode}-mode`);
        if (modeView) {
            modeView.classList.add('active');
        }
    }

    applyTheme(theme) {
        this.currentTheme = theme;
        document.body.setAttribute('data-theme', theme);
        
        // Update theme selector
        const themeSelect = document.getElementById('theme-select');
        if (themeSelect) {
            themeSelect.value = theme;
        }
    }

    handleButtonPress(action) {
        if (this.currentMode === 'standard' || this.currentMode === 'minimalist') {
            this.handleStandardButton(action);
        } else if (this.currentMode === 'scientific') {
            this.handleScientificButton(action);
        } else if (this.currentMode === 'programmer') {
            this.handleProgrammerButton(action);
        }
    }

    handleStandardButton(action) {
        const exprElement = document.getElementById(this.currentMode === 'minimalist' ? 'min-expr' : 'expr');
        const resultElement = document.getElementById(this.currentMode === 'minimalist' ? 'min-result' : 'result');

        switch (action) {
            case 'C':
                this.currentExpression = '';
                this.currentResult = '0';
                break;

            case 'backspace':
                this.currentExpression = this.currentExpression.slice(0, -1);
                break;

            case '=':
                try {
                    if (this.currentExpression) {
                        this.currentResult = this.mathEngine.evaluate(this.currentExpression);
                        this.lastResult = parseFloat(this.currentResult);
                        this.currentExpression = this.currentResult;
                    }
                } catch (error) {
                    this.currentResult = 'Error';
                }
                break;

            case 'negate':
                if (this.currentExpression) {
                    if (this.currentExpression.startsWith('-')) {
                        this.currentExpression = this.currentExpression.substring(1);
                    } else {
                        this.currentExpression = '(' + this.currentExpression + ')';
                        if (this.currentExpression.startsWith('(-')) {
                            this.currentExpression = this.currentExpression.substring(1);
                        } else {
                            this.currentExpression = '-' + this.currentExpression;
                        }
                    }
                } else if (this.currentResult !== '0' && this.currentResult !== 'Error') {
                    if (this.currentResult.startsWith('-')) {
                        this.currentResult = this.currentResult.substring(1);
                    } else {
                        this.currentResult = '-' + this.currentResult;
                    }
                    this.currentExpression = this.currentResult;
                }
                break;

            case 'MC':
            case 'MR':
            case 'M+':
            case 'M-':
            case 'MS':
                this.handleMemoryAction(action);
                this.refreshMemoryDisplay();
                break;

            default:
                this.currentExpression += action;
                break;
        }

        // Update display
        exprElement.textContent = this.currentExpression || '';
        resultElement.textContent = this.currentResult || '0';
    }

    handleScientificButton(action) {
        const exprElement = document.getElementById('sci-expr');
        const resultElement = document.getElementById('sci-result');

        switch (action) {
            case 'C':
                this.currentExpression = '';
                this.currentResult = '0';
                break;

            case 'backspace':
                this.currentExpression = this.currentExpression.slice(0, -1);
                break;

            case '=':
                try {
                    if (this.currentExpression) {
                        this.currentResult = this.mathEngine.evaluate(this.currentExpression);
                        this.lastResult = parseFloat(this.currentResult);
                        this.currentExpression = this.currentResult;
                    }
                } catch (error) {
                    this.currentResult = 'Error';
                }
                break;

            case 'negate':
                if (this.currentExpression.startsWith('-')) {
                    this.currentExpression = this.currentExpression.substring(1);
                } else {
                    this.currentExpression = '-' + this.currentExpression;
                }
                break;

            case 'pi':
                this.currentExpression += 'π';
                break;

            case 'e':
                this.currentExpression += 'e';
                break;

            case 'sqrt':
                this.currentExpression += 'sqrt(';
                break;

            case 'pow2':
                this.currentExpression += '**2';
                break;

            case '1/x':
                if (this.currentExpression) {
                    this.currentExpression = '1/(' + this.currentExpression + ')';
                }
                break;

            case 'exp':
                this.currentExpression += 'exp(';
                break;

            case '^':
                this.currentExpression += '**';
                break;

            case 'MC':
            case 'MR':
            case 'M+':
            case 'M-':
            case 'MS':
                this.handleMemoryAction(action);
                this.refreshMemoryDisplay();
                break;

            default:
                if (['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'ln'].includes(action)) {
                    this.currentExpression += action + '(';
                } else {
                    this.currentExpression += action;
                }
                break;
        }

        exprElement.textContent = this.currentExpression || '';
        resultElement.textContent = this.currentResult || '0';
    }

    handleProgrammerButton(action) {
        const exprElement = document.getElementById('prog-expr');
        const resultElement = document.getElementById('prog-result');

        switch (action) {
            case 'clear':
            case 'C':
                this.progExpression = '';
                this.progResult = '0';
                break;

            case 'backspace':
                this.progExpression = this.progExpression.slice(0, -1);
                break;

            case '=':
                try {
                    if (this.progExpression) {
                        this.progResult = this.mathEngine.evaluate(this.progExpression);
                        this.updateBaseIndicators(parseInt(this.progResult));
                    }
                } catch (error) {
                    this.progResult = 'Error';
                }
                break;

            case 'AND':
            case 'OR':
            case 'XOR':
            case 'NOT':
            case 'SHL':
                this.progExpression += ` ${action} `;
                break;

            case 'MC':
            case 'MR':
            case 'M+':
            case 'M-':
            case 'MS':
                this.handleMemoryAction(action);
                break;

            default:
                this.progExpression += action;
                break;
        }

        exprElement.textContent = this.progExpression;
        resultElement.textContent = this.progResult || '0';
    }

    updateBaseIndicators(value) {
        if (isNaN(value)) return;
        
        document.getElementById('hex-display').textContent = `HEX: ${this.mathEngine.toHex(value)}`;
        document.getElementById('dec-display').textContent = `DEC: ${this.mathEngine.toDec(value)}`;
        document.getElementById('oct-display').textContent = `OCT: ${this.mathEngine.toOct(value)}`;
        document.getElementById('bin-display').textContent = `BIN: ${this.mathEngine.toBin(value)}`;
    }

    handleMemoryAction(action) {
        switch (action) {
            case 'MC':
                this.memory = [];
                break;

            case 'MR':
                if (this.memory.length > 0) {
                    const value = this.memory[this.memory.length - 1];
                    this.currentExpression = value.toString();
                    this.currentResult = value.toString();
                }
                break;

            case 'M+':
                if (this.currentResult !== '0' && this.currentResult !== 'Error') {
                    const val = parseFloat(this.currentResult);
                    if (this.memory.length > 0) {
                        this.memory[this.memory.length - 1] += val;
                    } else {
                        this.memory.push(val);
                    }
                }
                break;

            case 'M-':
                if (this.currentResult !== '0' && this.currentResult !== 'Error') {
                    const val = parseFloat(this.currentResult);
                    if (this.memory.length > 0) {
                        this.memory[this.memory.length - 1] -= val;
                    } else {
                        this.memory.push(-val);
                    }
                }
                break;

            case 'MS':
                if (this.currentResult !== '0' && this.currentResult !== 'Error') {
                    this.memory.push(parseFloat(this.currentResult));
                }
                break;
        }
        
        this.saveMemory();
        this.refreshMemoryDisplay();
    }

    refreshMemoryDisplay() {
        const listContainer = document.getElementById('memory-list');
        listContainer.innerHTML = '';

        if (this.memory.length === 0) {
            listContainer.innerHTML = '<div class="memory-empty">No saved values<br><br>Use MS to save<br>the current value</div>';
            return;
        }

        this.memory.forEach((val, index) => {
            const item = document.createElement('div');
            item.className = 'memory-item';
            
            const displayVal = Number.isInteger(val) ? val.toString() : val.toLocaleString('en-US', { maximumSignificantDigits: 10 });
            
            item.innerHTML = `
                <span class="memory-index">M${index + 1}</span>
                <span class="memory-value">${displayVal}</span>
                <button class="memory-delete" data-index="${index}">✕</button>
            `;

            // Click to recall
            item.addEventListener('click', (e) => {
                if (e.target.classList.contains('memory-delete')) return;
                this.recallMemory(index);
            });

            // Delete button
            item.querySelector('.memory-delete').addEventListener('click', (e) => {
                e.stopPropagation();
                this.deleteMemory(index);
            });

            listContainer.appendChild(item);
        });
    }

    recallMemory(index) {
        if (index >= 0 && index < this.memory.length) {
            const value = this.memory[index];
            this.currentExpression = value.toString();
            this.currentResult = value.toString();
            
            // Update display based on current mode
            this.updateDisplayFromMemory();
        }
    }

    deleteMemory(index) {
        if (index >= 0 && index < this.memory.length) {
            this.memory.splice(index, 1);
            this.saveMemory();
            this.refreshMemoryDisplay();
        }
    }

    clearAllMemory() {
        this.memory = [];
        this.saveMemory();
        this.refreshMemoryDisplay();
    }

    updateDisplayFromMemory() {
        const mode = this.currentMode;
        let exprEl, resultEl;
        
        switch (mode) {
            case 'standard':
                exprEl = document.getElementById('expr');
                resultEl = document.getElementById('result');
                break;
            case 'scientific':
                exprEl = document.getElementById('sci-expr');
                resultEl = document.getElementById('sci-result');
                break;
            case 'programmer':
                exprEl = document.getElementById('prog-expr');
                resultEl = document.getElementById('prog-result');
                break;
            case 'minimalist':
                exprEl = document.getElementById('min-expr');
                resultEl = document.getElementById('min-result');
                break;
            default:
                return;
        }
        
        if (exprEl) exprEl.textContent = this.currentExpression;
        if (resultEl) resultEl.textContent = this.currentResult;
    }

    showMemoryPanel() {
        document.body.classList.remove('memory-panel-hidden');
        this.saveMemoryPanelState(true);
    }

    hideMemoryPanel() {
        document.body.classList.add('memory-panel-hidden');
        this.saveMemoryPanelState(false);
    }

    saveMemoryPanelState(visible) {
        try {
            localStorage.setItem('calc-memory-panel-visible', visible ? 'true' : 'false');
        } catch (error) {
            console.warn('Could not save memory panel state:', error);
        }
    }

    loadMemoryPanelState() {
        try {
            const saved = localStorage.getItem('calc-memory-panel-visible');
            if (saved === 'false') {
                document.body.classList.add('memory-panel-hidden');
            }
        } catch (error) {
            // Default to visible
        }
    }

    // Currency Converter Functions
    buildCurrencyList() {
        const listContainer = document.getElementById('currency-list');
        listContainer.innerHTML = '';

        const currencies = this.currencyConverter.getAllCurrencies();
        currencies.forEach(currency => {
            const item = document.createElement('div');
            item.className = 'currency-item';
            item.dataset.code = currency.code;
            item.innerHTML = `
                <div class="currency-icon">${currency.symbol}</div>
                <div class="currency-info">
                    <div class="currency-name">${currency.code} - ${currency.name}</div>
                    <div class="currency-rate">${currency.rate.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</div>
                </div>
            `;
            
            item.addEventListener('click', () => {
                this.handleCurrencySelect(currency.code);
            });

            listContainer.appendChild(item);
        });
    }

    filterCurrencyList(query) {
        const items = document.querySelectorAll('.currency-item');
        const lowerQuery = query.toLowerCase();

        items.forEach(item => {
            const code = item.dataset.code.toLowerCase();
            const name = item.querySelector('.currency-name').textContent.toLowerCase();
            const symbol = item.querySelector('.currency-icon').textContent.toLowerCase();

            const visible = code.includes(lowerQuery) || name.includes(lowerQuery) || symbol.includes(lowerQuery);
            item.style.display = visible ? 'flex' : 'none';
        });
    }

    handleCurrencySelect(code) {
        if (this.currencyConverter.selectMode === 'from') {
            this.currencyConverter.fromCurrency = code;
            this.currencyConverter.selectMode = 'to';
        } else {
            this.currencyConverter.toCurrency = code;
            this.currencyConverter.selectMode = 'from';
        }
        
        this.updateCurrencyDisplay();
        this.updateCurrencyConversion();
    }

    updateCurrencyDisplay() {
        document.querySelector('#from-currency .currency-code').textContent = this.currencyConverter.fromCurrency;
        document.querySelector('#to-currency .currency-code').textContent = this.currencyConverter.toCurrency;
    }

    updateCurrencyConversion() {
        const amountInput = document.getElementById('currency-amount');
        const resultElement = document.getElementById('currency-result');
        
        try {
            const amount = parseFloat(amountInput.value) || 0;
            this.currencyConverter.amount = amount;
            
            const result = this.currencyConverter.convert(
                amount,
                this.currencyConverter.fromCurrency,
                this.currencyConverter.toCurrency
            );

            const fromSym = CURRENCY_SYMBOLS[this.currencyConverter.fromCurrency] || this.currencyConverter.fromCurrency;
            const toSym = CURRENCY_SYMBOLS[this.currencyConverter.toCurrency] || this.currencyConverter.toCurrency;

            resultElement.textContent = `${fromSym}${amount.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })} ${this.currencyConverter.fromCurrency}\n=\n${toSym}${result.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })} ${this.currencyConverter.toCurrency}`;
        } catch (error) {
            resultElement.textContent = 'Invalid input';
        }
    }

    // Metric Converter Functions
    buildMetricUnitList() {
        const listContainer = document.getElementById('metric-unit-list');
        listContainer.innerHTML = '';

        const units = this.metricConverter.getAllUnits();
        units.forEach(unit => {
            const item = document.createElement('div');
            item.className = 'unit-item';
            item.textContent = unit.name;
            item.dataset.code = unit.code;

            item.addEventListener('click', () => {
                // Toggle between from and to unit
                if (this.metricConverter.fromUnit === unit.code) {
                    // Swap with another unit
                    const otherUnits = units.filter(u => u.code !== unit.code);
                    if (otherUnits.length > 0) {
                        this.metricConverter.toUnit = otherUnits[0].code;
                    }
                } else {
                    this.metricConverter.toUnit = unit.code;
                }
                this.updateMetricConversion();
            });

            listContainer.appendChild(item);
        });

        // Update labels
        document.getElementById('metric-from-label').textContent = this.metricConverter.getUnitName(this.metricConverter.fromUnit);
        document.getElementById('metric-to-label').textContent = this.metricConverter.getUnitName(this.metricConverter.toUnit);
    }

    updateMetricConversion() {
        const fromValue = parseFloat(document.getElementById('metric-from-value').value) || 0;
        
        try {
            const result = this.metricConverter.convert(
                fromValue,
                this.metricConverter.fromUnit,
                this.metricConverter.toUnit
            );

            document.getElementById('metric-to-value').value = result.toLocaleString('en-US', { maximumFractionDigits: 6 });
        } catch (error) {
            document.getElementById('metric-to-value').value = 'Error';
        }
    }

    // Temperature Converter Functions
    updateTemperatureFromCelsius(value) {
        const c = parseFloat(value);
        if (isNaN(c)) return;

        const f = TemperatureConverter.celsiusToFahrenheit(c);
        const k = TemperatureConverter.celsiusToKelvin(c);

        document.getElementById('temp-fahrenheit').value = f.toFixed(2);
        document.getElementById('temp-kelvin').value = k.toFixed(2);
    }

    updateTemperatureFromFahrenheit(value) {
        const f = parseFloat(value);
        if (isNaN(f)) return;

        const c = TemperatureConverter.fahrenheitToCelsius(f);
        const k = TemperatureConverter.fahrenheitToKelvin(f);

        document.getElementById('temp-celsius').value = c.toFixed(2);
        document.getElementById('temp-kelvin').value = k.toFixed(2);
    }

    updateTemperatureFromKelvin(value) {
        const k = parseFloat(value);
        if (isNaN(k)) return;

        const c = TemperatureConverter.kelvinToCelsius(k);
        const f = TemperatureConverter.kelvinToFahrenheit(k);

        document.getElementById('temp-celsius').value = c.toFixed(2);
        document.getElementById('temp-fahrenheit').value = f.toFixed(2);
    }

    // Storage Functions
    saveMemory() {
        try {
            localStorage.setItem('calc-memory', JSON.stringify(this.memory));
        } catch (error) {
            console.warn('Could not save memory:', error);
        }
    }

    loadMemory() {
        try {
            const saved = localStorage.getItem('calc-memory');
            if (saved) {
                this.memory = JSON.parse(saved);
            }
        } catch (error) {
            this.memory = [];
        }
    }

    saveTheme() {
        try {
            localStorage.setItem('calc-theme', this.currentTheme);
        } catch (error) {
            console.warn('Could not save theme:', error);
        }
    }

    loadTheme() {
        try {
            const saved = localStorage.getItem('calc-theme');
            if (saved) {
                this.currentTheme = saved;
            }
        } catch (error) {
            this.currentTheme = 'fluent-dark';
        }
    }
}

// Initialize calculator when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.calculator = new CalculatorApp();
});
