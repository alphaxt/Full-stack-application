# Screenshot Guide for Tasks 25-28

This guide provides detailed instructions for taking the required screenshots.

## General Screenshot Tips

1. **Use Full Screen**: Press F11 to enter fullscreen mode for cleaner screenshots
2. **Show Address Bar**: Make sure the browser address bar is visible
3. **Use PNG or JPG**: Save files as `.png` or `.jpg`
4. **Clear Browser**: Clear cache if pages don't load correctly
5. **Window Size**: Use a standard browser window size (not too small)

## Task 25: Landing Page Screenshot

### What to Capture:
- **URL in address bar**: Must be visible and match your deployment URL
- **Dealerships listing**: Should show multiple dealership cards
- **Navigation bar**: "About Us", "Contact Us", "Login", "Sign Up" links
- **State filter dropdown**: "Filter by State" form

### Steps:
1. Open your deployment URL: `http://localhost:8000/djangoapp/` (or your cloud URL)
2. Wait for page to fully load
3. Scroll to see multiple dealerships if needed
4. Take screenshot (Windows: `Win + Shift + S`, Mac: `Cmd + Shift + 4`)
5. Save as: `deployed_landingpage.png`

### Example URL Format:
- Local: `http://localhost:8000/djangoapp/`
- Cloud: `https://your-app.herokuapp.com/djangoapp/`

## Task 26: Logged-In Page Screenshot

### What to Capture:
- **URL in address bar**: Must match deployment URL
- **Username visible**: Should show in navigation (e.g., "John (john)")
- **"Post Review" buttons**: Should be visible next to each dealership
- **"Logout" link**: Should be in navigation bar
- **Dealerships listing**: Should still show dealerships

### Steps:
1. Make sure you're logged in
2. Navigate to: `{your-url}/djangoapp/`
3. Verify username is visible in top-right navigation
4. Verify "Post Review" buttons are visible
5. Take screenshot
6. Save as: `deployed_loggedin.png`

### What NOT to Include:
- Don't show the login form
- Don't show registration form
- Must show you're already logged in

## Task 27: Dealer Details Screenshot

### What to Capture:
- **URL in address bar**: Should be `/djangoapp/dealer/{id}/`
- **Dealer information**: Name, address, city, state
- **Reviews section**: Should show review cards
- **At least one review**: Must be visible
- **Sentiment emojis**: If reviews have sentiment analysis

### Steps:
1. Click on any dealership from the listing
2. Wait for dealer details page to load
3. Scroll to see reviews if needed
4. Make sure URL shows dealer ID (e.g., `/djangoapp/dealer/15/`)
5. Take screenshot
6. Save as: `deployed_dealer_detail.png`

### If No Reviews Show:
- That's okay, just show the dealer information
- The URL and dealer details are what matter

## Task 28: Review Added Screenshot

### What to Capture:
- **URL in address bar**: Should be `/djangoapp/dealer/{id}/`
- **Your new review**: Must be visible (usually at top of list)
- **Review content**: Should match what you entered
- **Your name**: Should be on the review card
- **Review details**: Purchase info if you included it

### Steps:
1. Click "Post Review" on any dealership
2. Fill out the form:
   - Enter review text (e.g., "Excellent service!")
   - Check "Has purchased" if you want
   - Select a car (add cars in admin first if needed)
   - Enter purchase date if purchased
3. Click "Submit"
4. After redirect, your review should be at the top
5. Take screenshot showing your review
6. Save as: `deployed_add_review.png`

### Important:
- The review you just added must be visible
- Review content should match what you typed
- URL must match the dealer details page

## Common Issues and Solutions

### Issue: URL Not Visible in Screenshot
**Solution**: 
- Don't use browser's screenshot tool that hides address bar
- Use OS screenshot tool (Win + Shift + S or Cmd + Shift + 4)
- Or use browser extension that shows address bar

### Issue: Screenshot Too Large
**Solution**:
- Crop to show relevant content
- Keep address bar visible
- Use image editor to resize if needed

### Issue: Wrong URL in Screenshot
**Solution**:
- Make sure you're using the same deployment URL for all screenshots
- If you changed deployment, update Task 24 URL first
- All screenshots must use the same base URL

### Issue: Can't See Required Elements
**Solution**:
- Zoom out (Ctrl + Minus or Cmd + Minus)
- Use larger browser window
- Scroll to show all required elements
- Take multiple screenshots if needed, but submit the best one

## Verification Checklist

Before submitting, check each screenshot:

### Task 25:
- [ ] URL visible and matches deployment URL
- [ ] Shows `/djangoapp/` in path
- [ ] Dealerships are visible
- [ ] Navigation bar is visible
- [ ] File named: `deployed_landingpage.png` or `.jpg`

### Task 26:
- [ ] URL visible and matches deployment URL
- [ ] Shows `/djangoapp/` in path
- [ ] Username visible in navigation
- [ ] "Post Review" buttons visible
- [ ] "Logout" link visible
- [ ] File named: `deployed_loggedin.png` or `.jpg`

### Task 27:
- [ ] URL visible and matches deployment URL
- [ ] Shows `/djangoapp/dealer/{id}/` in path
- [ ] Dealer information visible
- [ ] Reviews section visible
- [ ] File named: `deployed_dealer_detail.png` or `.jpg`

### Task 28:
- [ ] URL visible and matches deployment URL
- [ ] Shows `/djangoapp/dealer/{id}/` in path
- [ ] Your newly added review is visible
- [ ] Review content matches what you entered
- [ ] Your name is on the review
- [ ] File named: `deployed_add_review.png` or `.jpg`

## Example Screenshot Layouts

### Good Screenshot:
```
┌─────────────────────────────────────────┐
│ [Browser Address Bar with URL]          │
├─────────────────────────────────────────┤
│ [Navigation Bar]                        │
│ [Page Content - Dealerships/Reviews]    │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

### Bad Screenshot (Missing URL):
```
┌─────────────────────────────────────────┐
│ [Navigation Bar]                        │
│ [Page Content]                          │
│                                         │
└─────────────────────────────────────────┘
(No address bar - will be rejected)
```

## Tools for Screenshots

### Windows:
- **Snipping Tool**: `Win + Shift + S`
- **Print Screen**: `PrtScn` (captures full screen)
- **Windows + Shift + S**: Opens snipping tool

### Mac:
- **Cmd + Shift + 4**: Select area to screenshot
- **Cmd + Shift + 3**: Full screen screenshot
- **Cmd + Shift + 4 + Space**: Window screenshot

### Linux:
- **Print Screen**: Full screen
- **Shift + Print Screen**: Select area
- **Alt + Print Screen**: Current window

### Browser Extensions:
- Full Page Screen Capture (Chrome/Firefox)
- Awesome Screenshot
- Nimbus Screenshot

## Final Tips

1. **Test First**: Take test screenshots to ensure everything is visible
2. **Check Quality**: Make sure text is readable
3. **Verify URLs**: Double-check URLs match across all screenshots
4. **File Names**: Use exact names: `deployed_landingpage.png`, etc.
5. **File Size**: Keep files under 5MB if possible
6. **Format**: PNG is preferred, JPG is acceptable

Good luck! 🎯

