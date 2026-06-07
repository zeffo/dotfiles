#!/usr/bin/env nu

def main [...args: string] {
  let dev = (atmbrg scan-one | str trim)
  if ($dev | is-empty) {
    print "No device found"
    exit 1
  }
  ^atmbrg --device $dev ...$args
}
