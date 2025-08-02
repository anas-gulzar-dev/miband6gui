# Setup Guide for 160x28 Screen Users

## Quick Fix for "Window Too Small" Error

Your screen size of 160x28 was being rejected by the old validation logic. This has been fixed!

## Option 1: Use the Pre-configured Settings (Recommended)

1. Copy the optimized configuration file:
   ```bash
   copy .env.small_screen .env
   ```

2. Update your Azure credentials in the `.env` file:
   ```
   AZURE_API_KEY=your_actual_api_key_here
   AZURE_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Option 2: Use the UI Toggle (Instant Fix)

1. Start the application normally
2. Click the "⚠️ Small Window Warning: OFF" button in the top toolbar
3. The application will now work perfectly with your 160x28 screen!

## What Was Fixed

### Before (Problem):
- Minimum window size: 50x50 pixels
- Your screen (160x28) was rejected because height < 50
- Error: "Window too small: 160x28 (minimum 50x50)"

### After (Solution):
- **Minimum window size**: 10x10 pixels (configurable)
- **Your screen (160x28)**: ✅ Now fully supported!
- **Smart warnings**: Can be disabled with one click
- **Flexible validation**: Works with any screen size

## Configuration Options

Add these to your `.env` file for further customization:

```bash
# Minimum window size (very permissive)
MIN_WINDOW_WIDTH=10
MIN_WINDOW_HEIGHT=10

# Disable small window warnings
SHOW_SMALL_WINDOW_WARNING=false

# Small window warning thresholds
SMALL_WINDOW_WARNING_WIDTH=10
SMALL_WINDOW_WARNING_HEIGHT=10
```

## Features Added

1. **Configurable minimum window size** - Set as low as 5x5 pixels
2. **Runtime toggle** - Turn warnings on/off without restarting
3. **Smart validation** - Works with any screen size
4. **User-friendly messages** - Clear feedback about what's happening
5. **160x28 optimized defaults** - Perfect for your screen size

## Testing

The application will now:
- ✅ Detect your 160x28 window
- ✅ Allow screenshots without errors
- ✅ Show "Small window detected: 160x28 - capturing anyway" (if warnings enabled)
- ✅ Or work silently (if warnings disabled)

## Troubleshooting

If you still see issues:
1. Check that your `.env` file has the correct settings
2. Click the "⚠️ Small Window Warning: OFF" button
3. Verify your window is actually 160x28 by checking the device list
4. Try the "🔍 Show ALL Devices NOW" button to see all available windows

Your 160x28 screen is now fully supported! 🎉
