// Math Engine for Calculator
class MathEngine {
    constructor() {
        this.history = [];
        this.maxHistory = 100;
    }

    evaluate(expression) {
        try {
            let expr = expression.trim();
            if (!expr) return '';

            // Preprocess expression
            expr = this.preprocessExpression(expr);

            // Safe evaluation using Function constructor with restricted scope
            const result = this.safeEvaluate(expr);

            // Format result
            let resultStr;
            if (Number.isInteger(result)) {
                resultStr = result.toString();
            } else {
                resultStr = this.formatNumber(result);
            }

            // Add to history
            this.addToHistory(expression, resultStr);

            return resultStr;
        } catch (error) {
            throw new Error(`Invalid expression: ${expression}`);
        }
    }

    preprocessExpression(expr) {
        // Replace common math notation
        return expr
            .replace(/×/g, '*')
            .replace(/÷/g, '/')
            .replace(/−/g, '-')
            .replace(/(?<![a-zA-Z])e(?![a-zA-Z(])/g, Math.E.toString())
            .replace(/π/g, Math.PI.toString());
    }

    safeEvaluate(expr) {
        // Create safe evaluation context
        const safeMath = {
            sin: Math.sin,
            cos: Math.cos,
            tan: Math.tan,
            asin: Math.asin,
            acos: Math.acos,
            atan: Math.atan,
            log: Math.log10,
            ln: Math.log,
            sqrt: Math.sqrt,
            exp: Math.exp,
            abs: Math.abs,
            pow: Math.pow
        };

        // Replace function names with safeMath references
        let processedExpr = expr
            .replace(/\*\*/g, '__pow__')
            .replace(/sin\(/g, 'safeMath.sin(')
            .replace(/cos\(/g, 'safeMath.cos(')
            .replace(/tan\(/g, 'safeMath.tan(')
            .replace(/asin\(/g, 'safeMath.asin(')
            .replace(/acos\(/g, 'safeMath.acos(')
            .replace(/atan\(/g, 'safeMath.atan(')
            .replace(/log10\(/g, 'safeMath.log(')
            .replace(/log\(/g, 'safeMath.log(')
            .replace(/ln\(/g, 'safeMath.ln(')
            .replace(/sqrt\(/g, 'safeMath.sqrt(')
            .replace(/exp\(/g, 'safeMath.exp(')
            .replace(/abs\(/g, 'safeMath.abs(')
            .replace(/__pow__/g, 'safeMath.pow(');

        try {
            // eslint-disable-next-line no-new-func
            const func = new Function('safeMath', `return ${processedExpr};`);
            return func(safeMath);
        } catch (error) {
            throw new Error('Evaluation error');
        }
    }

    formatNumber(num) {
        if (!isFinite(num)) return 'Error';
        if (Number.isInteger(num)) return num.toString();
        
        // Remove trailing zeros
        let result = num.toPrecision(12);
        result = parseFloat(result).toString();
        
        return result;
    }

    addToHistory(expression, result) {
        this.history.push({ expression, result, timestamp: Date.now() });
        if (this.history.length > this.maxHistory) {
            this.history.shift();
        }
    }

    getHistory() {
        return [...this.history];
    }

    clearHistory() {
        this.history = [];
    }

    // Scientific functions
    factorial(n) {
        if (n < 0 || !Number.isInteger(n)) throw new Error('Invalid input');
        if (n === 0 || n === 1) return 1;
        let result = 1;
        for (let i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    power(base, exponent) {
        return Math.pow(base, exponent);
    }

    // Bitwise operations for programmer mode
    bitwiseAnd(a, b) { return a & b; }
    bitwiseOr(a, b) { return a | b; }
    bitwiseXor(a, b) { return a ^ b; }
    bitwiseNot(a) { return ~a; }
    shiftLeft(a, b) { return a << b; }
    shiftRight(a, b) { return a >> b; }

    // Base conversion
    toHex(num) {
        return '0x' + (num >>> 0).toString(16).toUpperCase();
    }

    toOct(num) {
        return '0o' + (num >>> 0).toString(8);
    }

    toBin(num) {
        return '0b' + (num >>> 0).toString(2);
    }

    toDec(num) {
        return num >>> 0;
    }
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = MathEngine;
}
