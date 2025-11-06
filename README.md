# Conversor de Unidades con FastAPI y CI/CD

Un **conversor de unidades** moderno y eficiente para temperatura y distancia, desarrollado con  **FastAPI** , e implementando un pipeline completo de **Integración Continua y Entrega Continua (CI/CD)** con **GitHub Actions** y análisis de seguridad con  **CodeQL** .

---

## 🚀 Características

### Conversiones Disponibles

* **Temperatura:** Celsius ↔ Fahrenheit
* **Distancia:** Kilómetros ↔ Millas

### API REST

* Endpoints intuitivos y documentados
* Respuestas JSON
* Validación automática de parámetros
* Documentación interactiva (Swagger UI y ReDoc)

---

## 🩺 Endpoint de Salud

**`/health`**

* Retorna `{"status": "ok", "timestamp": "2025-01-01T12:00:00Z"}`
* Incluye `"api_key_configurada": true` si existe la variable `MY_API_KEY`
* Ideal para monitoreo y validaciones automáticas en pipelines

---

## 🧩 Endpoints de Monitoreo y Auditoría

### `/ping`

* **Método:** `GET`
* **Descripción:** Guarda información de la petición (IP, timestamp, API key) en **Redis** y base de datos.
* Permite auditar accesos y verificar el estado del servicio.
* Requiere token válido.

**Ejemplo de respuesta:**

<pre class="overflow-visible!" data-start="1445" data-end="1544"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"status"</span><span>:</span><span></span><span>"ok"</span><span>,</span><span>
  </span><span>"timestamp"</span><span>:</span><span></span><span>"2025-11-06T15:00:00Z"</span><span>,</span><span>
  </span><span>"client_ip"</span><span>:</span><span></span><span>"127.0.0.1"</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

---

### `/get-responses`

* **Método:** `GET`
* **Descripción:** Devuelve todos los registros almacenados por las llamadas a `/ping`.
* **Protegido** : requiere token válido (`Authorization: Bearer <token>`).

**Ejemplo:**

<pre class="overflow-visible!" data-start="1776" data-end="1949"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"total"</span><span>:</span><span></span><span>3</span><span>,</span><span>
  </span><span>"records"</span><span>:</span><span></span><span>[</span><span>
    </span><span>{</span><span>
      </span><span>"timestamp"</span><span>:</span><span></span><span>"2025-11-06T18:50:25.274221"</span><span>,</span><span>
      </span><span>"client_ip"</span><span>:</span><span></span><span>"127.0.0.1"</span><span>,</span><span>
      </span><span>"api_key"</span><span>:</span><span></span><span>"123456abcdef"</span><span>
    </span><span>}</span><span>
  </span><span>]</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

---

### `/clear-responses`

**Objetivo:**

Permite **eliminar todos los registros** almacenados en Redis o base de datos.

* **Método:** `DELETE`
* **Ruta:** `/clear-responses`
* **Protegido:** requiere token válido
* **Respuesta ejemplo:**

<pre class="overflow-visible!" data-start="2195" data-end="2270"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"message"</span><span>:</span><span></span><span>"All responses have been cleared successfully"</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

---

## 🔑 Autenticación con Token

* Endpoints `/ping`, `/get-responses` y `/clear-responses` requieren un  **token** .
* Los tokens válidos se guardan en Redis como `token:<valor>`.

**Ejemplo de uso:**

<pre class="overflow-visible!" data-start="2478" data-end="2583"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>curl -X GET </span><span>"http://127.0.0.1:8000/get-responses"</span><span> \
  -H </span><span>"Authorization: Bearer 123456abcdef"</span><span>
</span></span></code></div></div></pre>

**Ejemplo para crear token manualmente (Windows con Docker Redis):**

<pre class="overflow-visible!" data-start="2654" data-end="2727"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>docker </span><span>exec</span><span> -it redis redis-cli </span><span>set</span><span> token:123456abcdef </span><span>"true"</span><span>
</span></span></code></div></div></pre>

**Generar tokens JWT de ejemplo:**

👉 [https://www.jwt.io/](https://www.jwt.io/)

---

## 🔍 Análisis de Seguridad con CodeQL

Este proyecto utiliza **CodeQL** de GitHub para análisis estático automatizado de seguridad.

**Objetivo:**

> Detectar vulnerabilidades, malas prácticas y asegurar cumplimiento de estándares.

### Workflow CodeQL

Archivo: `.github/workflows/codeql.yml`

<pre class="overflow-visible!" data-start="3113" data-end="3863"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-yaml"><span><span>name:</span><span></span><span>"CodeQL"</span><span>

</span><span>on:</span><span>
  </span><span>push:</span><span>
    </span><span>branches:</span><span> [ </span><span>main</span><span> ]
  </span><span>pull_request:</span><span>
    </span><span>branches:</span><span> [ </span><span>main</span><span> ]
  </span><span>schedule:</span><span>
    </span><span>-</span><span></span><span>cron:</span><span></span><span>'0 3 * * 1'</span><span>

</span><span>jobs:</span><span>
  </span><span>analyze:</span><span>
    </span><span>name:</span><span></span><span>CodeQL</span><span></span><span>Analysis</span><span>
    </span><span>runs-on:</span><span></span><span>ubuntu-latest</span><span>
    </span><span>permissions:</span><span>
      </span><span>actions:</span><span></span><span>read</span><span>
      </span><span>contents:</span><span></span><span>read</span><span>
      </span><span>security-events:</span><span></span><span>write</span><span>

    </span><span>strategy:</span><span>
      </span><span>fail-fast:</span><span></span><span>false</span><span>
      </span><span>matrix:</span><span>
        </span><span>language:</span><span> [ </span><span>'python'</span><span> ]

    </span><span>steps:</span><span>
      </span><span>-</span><span></span><span>name:</span><span></span><span>Checkout</span><span></span><span>repository</span><span>
        </span><span>uses:</span><span></span><span>actions/checkout@v4</span><span>

      </span><span>-</span><span></span><span>name:</span><span></span><span>Initialize</span><span></span><span>CodeQL</span><span>
        </span><span>uses:</span><span></span><span>github/codeql-action/init@v3</span><span>
        </span><span>with:</span><span>
          </span><span>languages:</span><span></span><span>${{</span><span></span><span>matrix.language</span><span></span><span>}}</span><span>

      </span><span>-</span><span></span><span>name:</span><span></span><span>Autobuild</span><span>
        </span><span>uses:</span><span></span><span>github/codeql-action/autobuild@v3</span><span>

      </span><span>-</span><span></span><span>name:</span><span></span><span>Perform</span><span></span><span>CodeQL</span><span></span><span>Analysis</span><span>
        </span><span>uses:</span><span></span><span>github/codeql-action/analyze@v3</span><span>
</span></span></code></div></div></pre>

---

## 🧪 Testing

### Ejecutar tests

<pre class="overflow-visible!" data-start="3905" data-end="3958"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pytest
pytest --cov=app --cov-report=term
</span></span></code></div></div></pre>

### Cobertura

* Cobertura mínima requerida: **90%**
* Tests incluidos:
  * Conversión de temperatura y distancia
  * `/health`
  * `/ping` (con token)
  * `/get-responses` (con token)
  * `/clear-responses` (con token)

---

## 🐳 Uso con Docker

1. **Construir contenedores:**
   <pre class="overflow-visible!" data-start="4242" data-end="4280"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>docker-compose build
   </span></span></code></div></div></pre>
2. **Levantar servicios:**
   <pre class="overflow-visible!" data-start="4311" data-end="4346"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>docker-compose up
   </span></span></code></div></div></pre>
3. **Acceder a la API:**
   * Health → [http://localhost:8000/health](http://localhost:8000/health)
   * Ping → [http://localhost:8000/ping](http://localhost:8000/ping)
4. **Detener:**
   <pre class="overflow-visible!" data-start="4535" data-end="4572"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>docker-compose down
   </span></span></code></div></div></pre>

---

## ⚙️ CI/CD Pipeline

### Workflow principal (`.github/workflows/ci.yml`)

1. **Setup** Python
2. **Instala dependencias**
3. **Linting** con `flake8`
4. **Testing** con `pytest`
5. **Cobertura mínima** 90%
6. **Build y artifacts**
7. **Análisis CodeQL**

### Badges

<pre class="overflow-visible!" data-start="4861" data-end="5161"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-markdown"><span><span>![</span><span>CI</span><span>](</span><span>https://github.com/usuario/conversor-actions/workflows/CI/badge.svg</span><span>)
![</span><span>CodeQL</span><span>](</span><span>https://github.com/usuario/conversor-actions/workflows/CodeQL/badge.svg</span><span>)
![</span><span>Coverage</span><span>](</span><span>https://img.shields.io/badge/coverage-100%25-brightgreen</span><span>)
![</span><span>Python</span><span>](</span><span>https://img.shields.io/badge/python-3.8+-blue</span><span>)
</span></span></code></div></div></pre>

---

## 🏗️ Estructura del Proyecto

<pre class="overflow-visible!" data-start="5200" data-end="5711"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>conversor-actions/
├── app/
│   ├── __init__.py
│   ├── main.py              </span><span># FastAPI principal</span><span>
│   ├── conversor.py         </span><span># Lógica de conversiones</span><span>
│   └── database.py          </span><span># Conexión Redis y base de datos</span><span>
├── tests/
│   ├── test_api.py
│   ├── test_conversor.py
│   ├── test_health.py
│   ├── test_ping.py
│   ├── test_get_responses.py
│   └── test_clear_responses.py
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── codeql.yml
├── requirements.txt
├── pyproject.toml
└── README.md
</span></span></code></div></div></pre>

---

## 💡 Estándares de Código

* Cumple **PEP 8**
* Cobertura de tests ≥ 90%
* Sin errores de lint (`flake8`)
* Análisis estático automatizado con **CodeQL**
* Tokens seguros y validados en Redis
