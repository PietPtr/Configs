import XMonad
import XMonad.Hooks.ManageDocks
import XMonad.Layout.Spacing

main = xmonad defaultConfig
     { terminal    = "xterm"
     , normalBorderColor = "#445fa2" -- color of non-focused borders
     , focusedBorderColor = "#ada021" -- color of focused borders
     , startupHook = spawn "~/.xmonad/autostart.sh"
     , layoutHook = myLayoutHook
     -- ^ let the layout make space for bars
     }

myLayoutHook = avoidStruts (tiled ||| Mirror tiled) ||| Full
  where
    tiled = smartSpacing 4 -- het aantal pixels tussen windows
          $ Tall nmaster delta ratio
    nmaster = 1
    ratio = 3/5
    delta = 2/100
