from sorl.thumbnail.engines.pil_engine import Engine as PILEngine

class Engine(PILEngine):
    def create(self, image, geometry, options):
        if 'crop' not in options or options['crop'] != 'natural':
            return super(Engine, self).create(image, geometry, options)
        else:
            options['upscale'] = True
            image = self.colorspace(image, geometry, options)
            image = self.scale(image, geometry, options)
            image = self.crop_natural(image, geometry, options)
            return image

    def crop_natural(self, image, geometry, options):
        x_geom, y_geom = geometry
        x_image, y_image = self.get_image_size(image)
        if (x_image > x_geom):#picture is more horizontal then we need
            x_offset = int(round((x_image - x_geom)/2)) #crop left and right
            y_offset = 0
        else:#picture is more vertical then we need
            x_offset = y_offset = 0 #crop top part because heads are usually on top, unless you're in Australia
        return self._crop(image, geometry[0], geometry[1], x_offset, y_offset)
