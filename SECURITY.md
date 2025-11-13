# Security Policy

## Supported Versions

We actively support the following versions of Vyte with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| \< 2.0  | :x:                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue in Vyte, please report it responsibly.

### 🔒 Private Disclosure

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of these methods:

1. **Email**: Send details to Domi@usal.es

   - Subject: `[SECURITY] Vyte Vulnerability Report`
   - Include detailed description of the vulnerability
   - Steps to reproduce
   - Potential impact assessment
   - Suggested fix (if any)

1. **GitHub Security Advisory**: Use GitHub's [private vulnerability reporting](https://github.com/PabloDomi/Vyte/security/advisories/new)

### ⏱️ Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 5 business days
- **Fix Timeline**: Depends on severity
  - Critical: Within 7 days
  - High: Within 14 days
  - Medium: Within 30 days
  - Low: Next regular release

### 📋 What to Include

Please include as much information as possible:

1. **Type of vulnerability** (e.g., code injection, path traversal, etc.)
1. **Full paths** of source files related to the vulnerability
1. **Location** of the affected source code (tag/branch/commit)
1. **Step-by-step instructions** to reproduce the issue
1. **Proof-of-concept or exploit code** (if possible)
1. **Impact** of the vulnerability
1. **Possible mitigation** or workarounds

### 🎖️ Vulnerability Disclosure Process

1. **Report Received**: We acknowledge receipt of your vulnerability report
1. **Investigation**: We investigate and validate the vulnerability
1. **Fix Development**: We develop and test a fix
1. **Notification**: We notify you when the fix is ready
1. **Release**: We release a patch and security advisory
1. **Recognition**: We credit you in the security advisory (unless you prefer to remain anonymous)

### 🏆 Security Researcher Recognition

We appreciate security researchers who help keep Vyte secure. With your permission, we will:

- Credit you in the security advisory
- Mention you in the release notes
- Add you to our security hall of fame (if we create one)

## 🛡️ Security Best Practices for Users

### Generated Projects

When using Vyte to generate projects:

1. **Environment Variables**:

   - Never commit `.env` files to version control
   - Use strong, unique values for `JWT_SECRET_KEY`
   - Rotate secrets regularly

1. **Dependencies**:

   - Keep dependencies updated
   - Run `pip-audit` or `safety check` regularly
   - Review generated `requirements.txt`

1. **Database Credentials**:

   - Use strong passwords
   - Never use default credentials in production
   - Use environment variables for database URLs

1. **JWT Tokens**:

   - Use strong secret keys (minimum 32 characters)
   - Set appropriate expiration times
   - Implement token refresh mechanisms

1. **Docker**:

   - Don't run containers as root
   - Scan images for vulnerabilities
   - Keep base images updated

### Vyte CLI

When using Vyte CLI:

1. **Installation**:

   - Install from official sources (PyPI)
   - Verify package signatures if available
   - Use virtual environments

1. **Project Generation**:

   - Review generated code before deployment
   - Customize security settings for your needs
   - Remove unused features to reduce attack surface

## 🔐 Known Security Considerations

### Template Injection

Vyte uses Jinja2 for templating. We have taken precautions to prevent template injection:

- Templates are bundled with the package
- User input is sanitized before template rendering
- No user-provided templates are executed

### Path Traversal

Project names and paths are validated to prevent path traversal attacks:

- Restricted character sets for project names
- Absolute path resolution
- Validation before file operations

### Dependency Security

We regularly monitor and update dependencies to address known vulnerabilities.

Generated projects include:

- Latest stable versions of frameworks
- Security-focused defaults
- Dependency pinning for reproducibility

## 📚 Security Resources

### For Generated Projects

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [Flask Security](https://flask.palletsprojects.com/en/latest/security/)
- [Django Security](https://docs.djangoproject.com/en/stable/topics/security/)

### Tools for Security Scanning

```bash
# Python dependency vulnerabilities
pip install pip-audit
pip-audit

# Alternative
pip install safety
safety check

# Code security analysis
pip install bandit
bandit -r src/

# Secret scanning
pip install detect-secrets
detect-secrets scan
```

## 🔄 Security Updates

Subscribe to security updates:

1. **GitHub**: Watch the repository for security advisories
1. **PyPI**: Monitor package updates
1. **Email**: Contact us to join security mailing list

## ❓ Questions?

If you have questions about:

- This security policy
- Security features in Vyte
- Security best practices for generated projects

Please contact: Domi@usal.es

______________________________________________________________________

**Note**: This security policy applies to the Vyte CLI tool itself. Generated projects should establish their own security policies based on their specific requirements.

Thank you for helping keep Vyte and its users safe! 🛡️
