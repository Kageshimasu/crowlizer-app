export function preventTypingExceptNumber (evt: KeyboardEvent) {
  const keyCode = (evt.keyCode ? evt.keyCode : evt.which)
  if ((keyCode < 48 || keyCode > 57)) {
    evt.preventDefault()
  }
}
