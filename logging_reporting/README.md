# 🚀 Singleton Logger Implementation

![](https://github.com/yourusername/singleton-logger/actions/workflows/maven.yml/badge.svg)
![Java Version](https://img.shields.io/badge/Java-17%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Профессиональная реализация паттерна Singleton в Java с двумя подходами: классическим и потокобезопасным через enum.

## 🌟 Особенности

| Функция | Описание |
|---------|----------|
| **Двойная реализация** | Классический Singleton и потокобезопасный enum вариант |
| **Логирование** | Поддержка INFO и ERROR сообщений с временными метками |
| **Готовность к работе** | Полностью настроенный Maven/Gradle проект |
| **Документация** | Подробные комментарии в коде |

## 🛠 Реализации

### Классический Singleton (`AppLogger.java`)

```java
/**
 * Классическая реализация Singleton с ленивой инициализацией
 */
public class AppLogger {
    private static volatile AppLogger instance;
    
    private AppLogger() {
        // Защита от рефлексии
        if (instance != null) {
            throw new IllegalStateException("Уже инициализирован");
        }
    }
    
    public static AppLogger getInstance() {
        if (instance == null) {
            synchronized (AppLogger.class) {
                if (instance == null) {
                    instance = new AppLogger();
                }
            }
        }
        return instance;
    }
}
