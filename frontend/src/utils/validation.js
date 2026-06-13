/**
 * Email validation
 * @param {string} email - Email to validate
 * @returns {boolean} - True if valid
 */
export const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(email)
}

/**
 * Password validation
 * @param {string} password - Password to validate
 * @returns {boolean} - True if at least 8 characters
 */
export const validatePassword = (password) => {
  return password.length >= 8
}

/**
 * Phone number validation
 * @param {string} phone - Phone number to validate
 * @returns {boolean} - True if valid
 */
export const validatePhone = (phone) => {
  const phoneRegex = /^[0-9+\-\s()]{10,}$/
  return phoneRegex.test(phone)
}

/**
 * Name validation
 * @param {string} name - Name to validate
 * @returns {boolean} - True if valid
 */
export const validateName = (name) => {
  return name.trim().length >= 2
}

/**
 * URL validation
 * @param {string} url - URL to validate
 * @returns {boolean} - True if valid
 */
export const validateURL = (url) => {
  try {
    new URL(url)
    return true
  } catch {
    return false
  }
}

/**
 * Form validation helper
 * @param {object} data - Form data to validate
 * @param {object} rules - Validation rules
 * @returns {object} - Errors object
 */
export const validateForm = (data, rules) => {
  const errors = {}

  Object.keys(rules).forEach(field => {
    const rule = rules[field]
    const value = data[field]

    if (rule.required && (!value || value.trim() === '')) {
      errors[field] = rule.requiredMessage || `${field} is required`
    } else if (value && rule.pattern && !rule.pattern.test(value)) {
      errors[field] = rule.patternMessage || `${field} is invalid`
    } else if (value && rule.minLength && value.length < rule.minLength) {
      errors[field] = rule.minLengthMessage || `${field} must be at least ${rule.minLength} characters`
    } else if (value && rule.maxLength && value.length > rule.maxLength) {
      errors[field] = rule.maxLengthMessage || `${field} must be at most ${rule.maxLength} characters`
    }
  })

  return errors
}
