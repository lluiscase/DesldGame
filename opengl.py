phong_vertex = """
varying vec3 normalInterp;
varying vec3 vertPos;
void main() {
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    vertPos = vec3(gl_ModelViewMatrix * gl_Vertex);
    normalInterp = normalize(gl_NormalMatrix * gl_Normal);
}
"""

phong_fragment = """
varying vec3 normalInterp;
varying vec3 vertPos;
void main() {
    vec3 lightPos = vec3(0.0, 0.0, 2.0);
    vec3 N = normalize(normalInterp);
    vec3 L = normalize(lightPos - vertPos);
    float lambertian = max(dot(N, L), 0.0);
    vec3 R = reflect(-L, N);
    vec3 V = normalize(-vertPos);
    float specular = pow(max(dot(R, V), 0.0), 20.0);
    gl_FragColor = vec4(lambertian + specular, lambertian, lambertian, 1.0);
}
"""
gouraud_vertex = """
varying vec4 color;
void main(){
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    vec3 N = normalize(gl_NormalMatrix * gl_Normal);
    vec3 L = normalize(vec3(0.0, 0.0, 2.0) - vec3(gl_ModelViewMatrix * gl_Vertex));
    float intensity = max(dot(N, L), 0.0);
    color = vec4(intensity, intensity, intensity, 1.0);
}
"""

gouraud_fragment = """
varying vec4 color;
void main() {
    gl_FragColor = color;
}
"""
libertiano_vertex = """
varying float intensity;
void main() {
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    vec3 N = normalize(gl_NormalMatrix * gl_Normal);
    vec3 L = normalize(vec3(0.0,0.0,2.0) - vec3(gl_ModelViewMatrix * gl_Vertex));
    intensity = max(dot(N, L), 0.0);
}
"""

libertiano_fragment = """
varying float intensity;
void main() {
    gl_FragColor = vec4(intensity, intensity, intensity, 1.0);
}
"""
