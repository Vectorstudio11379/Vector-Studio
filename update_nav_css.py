# Script to update vector-nav.css with rainbow button styles

with open('vector-nav.css', 'r', encoding='utf-8') as f:
    content = f.read()

rainbow_css = """/* Rainbow Chromatic Gradient CTA Button */
.btn-primary:before {
  top: 0;
  left: -3px;
  transform: rotate(-45deg);
  transform-origin: top right;
  background: linear-gradient(to right, #ff007a 0%, #ff8a00 100%);
}
.btn-primary:after {
  bottom: 0;
  right: -3px;
  transform: rotate(-45deg);
  transform-origin: bottom left;
  background: linear-gradient(to right, #00ffa3 0%, #00e1ff 100%);
}
.btn-primary-lines-1:before,
.btn-primary-lines-1:after {
  position: absolute;
  width: calc(100% - 8px);
  height: 1.5px;
  content: "";
}
.btn-primary-lines-1:before {
  top: 0;
  left: 7px;
  background: linear-gradient(to right, #ff007a 0%, #ff8a00 35%, #ffe600 70%, #00ffa3 100%);
}
.btn-primary-lines-1:after {
  bottom: 0;
  right: 7px;
  background: linear-gradient(to right, #7928ca 0%, #00e1ff 50%, #00ffa3 100%);
}
.btn-primary-lines-2:before,
.btn-primary-lines-2:after {
  position: absolute;
  width: 1.5px;
  content: "";
}
.btn-primary-lines-2:before {
  bottom: 0;
  left: 0;
  height: 60%;
  background: linear-gradient(to bottom, #ff007a 0%, #7928ca 100%);
}
.btn-primary-lines-2:after {
  top: 0;
  right: 0;
  height: calc(100% - 7px);
  background: linear-gradient(to bottom, #00ffa3 0%, #00e1ff 100%);
}
.btn-primary-text {
  position: relative;
  display: inline-flex;
  align-items: center;
  padding-left: 1.25rem;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 13.5px;
  letter-spacing: 0.05em;
  color: #ffffff;
  text-transform: uppercase;
}
.btn-primary-text:before,
.btn-primary-text:after {
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto 0;
  width: 0.3rem;
  height: 0.3rem;
  border-radius: 50%;
  content: "";
}
.btn-primary-text:before {
  left: 0;
  background-color: #ff007a;
  box-shadow: 0 0 6px #ff007a;
}
.btn-primary-text:after {
  left: 0.5rem;
  background-color: #00e1ff;
  box-shadow: 0 0 6px #00e1ff;
}

.btn-primary:hover {
  background: rgba(255, 0, 122, 0.08);
  box-shadow: 0 0 25px rgba(255, 0, 122, 0.35), 0 0 45px rgba(0, 225, 255, 0.2);
}
"""

idx = content.find('.btn-primary:before')
if idx != -1:
    content = content[:idx] + rainbow_css
    with open('vector-nav.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated vector-nav.css with rainbow button styles")
else:
    print("Target .btn-primary:before not found")
