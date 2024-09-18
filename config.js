// Configuration settings for JavaScript application

const config = {
    // API settings
    api: {
        baseUrl: "https://api.example.com",
        apiKey: "your_api_key_here",
        timeout: 30000 // Timeout in milliseconds
    },

    // Database settings
    database: {
        host: "localhost",
        port: 5432,
        username: "admin",
        password: "password",
        name: "sample_db"
    },

    // Logging settings
    logging: {
        level: "info",
        file: "/var/log/app.log",
        maxSize: 10 * 1024 * 1024, // 10 MB
        backupCount: 5
    }
};

module.exports = config;
