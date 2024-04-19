const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'API Documentation',
      version: '1.0.0',
      description: 'Documentación de la API',
    },
    servers: [
      {
        url: 'http://localhost:4000', // Reemplaza esto con la URL de tu servidor
      },
    ],
  },
  apis: ['./src/*.js'], // Rutas de los archivos que contienen la documentación Swagger
};

const specs = swaggerJsdoc(options);

module.exports = (app) => {
  app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(specs));
};